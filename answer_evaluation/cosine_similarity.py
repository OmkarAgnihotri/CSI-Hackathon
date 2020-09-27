import re
import math
import numpy as np
# lemmatization library
import spacy
from collections import Counter

from nltk.corpus import stopwords

#tokenization library
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics.pairwise import cosine_similarity

# remove punctuations from the text
def regex_cleaning(text):
    pattern = re.compile(r'[\[\]\\,.!?\/\'():\"-]')
    return pattern.sub(' ',text)

def tokenization(text):
    # stop = stopwords.words('english')
    cv = CountVectorizer()
    count_vector = cv.fit_transform(np.array([text]))
    # print(cv.vocabulary_)
    # print(type(count_vector))
    return cv.vocabulary_
    
def lemmatization(text):
    nlp = spacy.load('en',disable = ['parser','ner'])
    doc = nlp(text)
    return " ".join([word.lemma_ for word in doc if word.lemma_ != '-PRON-'])

def cos(text,answer):
    v1 = text_to_vector(text)
    v2 = text_to_vector(answer)
    return get_category(get_cosine(v1,v2))

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    text = regex_cleaning(text.lower())
    text = lemmatization(text)
    vector = tokenization(text)
    return vector

def get_category(similarity):
    cosine = round(similarity,2)*100
    
    kval = 0
    if cosine > 90:
        kval = 1
    elif cosine > 80:
        kval = 2
    elif cosine > 60:
        kval = 3
    elif cosine > 40:
        kval = 4
    elif cosine > 20:
        kval = 5
    else:
        kval = 6
    return kval
