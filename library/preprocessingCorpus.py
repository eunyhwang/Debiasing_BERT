import pandas as pd
import argparse

# process corpus to prepare a list of target/ attribute words

def get_names():
    eec = pd.read_csv('Equity-Evaluation-Corpus.csv')
    african_american = eec[eec.Race == 'African-American']  # find the line which is african-american and european
    european = eec[eec.Race == 'European']

    african_american_names = african_american.Person.unique()
    european_names = european.Person.unique()

    #print("african_american:", african_american_names)
    #print("european:", european_names)
    return african_american_names, european_names

def get_emotion_words():
    eec = pd.read_csv('Equity-Evaluation-Corpus.csv')
    emotion_words = eec['Emotion word'].values.tolist()
    emotion_words = list(set(emotion_words))

    return emotion_words

def get_template():
    eec = pd.read_csv('Equity-Evaluation-Corpus.csv')
    template = eec.Template.unique()

    return template

