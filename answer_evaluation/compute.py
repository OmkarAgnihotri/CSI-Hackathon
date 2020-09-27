from cosine_similarity import *
from grammar import *
from qst import match_score
import pandas as pd

from sklearn.naive_bayes import MultinomialNB

class Classifier():
    def fit(self,text,answer):
        i = cos(text, answer)
        j = errors(text)
        k = match_score(text,answer)

        if i == 6 and j > 5:
            j = 0
        else:
            j = 1

        self.x1 = i
        self.x2 = j
        self.x3 = k
        print(i,j,k)

    def predict(self):
        df = pd.read_csv('finaldataset.csv')
        X = df.iloc[:,:-1].to_numpy()
        Y = df.iloc[:,-1].to_numpy()
        classifier = MultinomialNB()
        classifier.fit(X,Y)
        print(classifier.predict([[self.x1,self.x2,self.x3]]))