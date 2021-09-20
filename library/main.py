import pandas as pd

eec = pd.read_csv('Equity-Evaluation-Corpus.csv')

african_american = eec[eec.Race == 'African-American']  # find the line which is african-american and european
european = eec[eec.Race == 'European']
african_american_names = african_american.Person.unique()
european_names = european.Person.unique()

emotion_words = eec['Emotion word'].values.tolist()
emotion_words = list(set(emotion_words))

template = eec.Template.unique()
# <person subject> feels <emotion word>: ndarray
#print(i) for i in emotion_words]
#print(list)
print(template.type())
for i in template:
    sentence = []
    i.replace(f'<emotion word>', i for i in emotion_words)

#sentence = template.replace(r'<emotion word>', (i for i in emotion_words))