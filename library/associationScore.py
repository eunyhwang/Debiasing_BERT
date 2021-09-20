#calculate association score given sentence, sentence_masked, target_words

def get_prob(sentence, target_word):
    input_ids = tokenizer.encode(sentence, return_tensors='pt')
    mask_token_index = torch.where(input_ids == tokenizer.mask_token_id)[1]  # mask's position 0 or 1?

    token_logits = model(input_ids)[0]
    mask_token_logits = token_logits[0, mask_token_index, :]  # get the logits
    mask_token_logits = torch.softmax(mask_token_logits, dim=1)  # to get probability, apply softmax on the logits

    target_word_id = tokenizer.encode(target_word, add_special_tokens=False)[0]
    token_prob = mask_token_logits[:, target_word_id].detach().numpy()[0]

    return token_prob


def score(sentence, sentence_masked, target_word):
    #sample_sentence = f"{tokenizer.mask_token} is happy."
    #sample_sentence_masked = f"{tokenizer.mask_token} is {tokenizer.mask_token}."
    #sample_aw = "Brad"
    #sample_afw = "Hakim"
    prob = get_prob(sentence, target_word)
    prior_prob = get_prob(sentence_masked, target_word)
    association = np.log(prob / prior_prob)

    return association