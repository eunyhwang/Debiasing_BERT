import numpy as np
import torch

#install pre-trained transformers

from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline #what is the difference between this model with the others?

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased") #bert-base-uncased: This model is not case-sensitive: it doesn't make a difference between english and English.
model = AutoModelWithLMHead.from_pretrained("bert-base-uncased")

