import nltk
import random
from nltk.corpus import movie_reviews
import pickle

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:2000]

### Lesson: Converting words into Features
def find_features(document):
    words = set(document)  ## Change word tokens from document into a set 
    features = {}
    for w in word_features:
        features[w] = (w in words)   ## For each word in top 3000 list, check whether it is in the document - True or False

    return features

## print((find_features(movie_reviews.words('neg/cv160_10848.txt')))) ## Negative data set, one file 29416

## Convert document words into features
featuresets = [(find_features(rev), category) for (rev, category) in documents]

testing_set = featuresets[:200]
pickle_file = open("naivebayes.pickle","rb")
classifier = pickle.load(pickle_file)
pickle_file.close()

print("Classifer accuracy percent:",(nltk.classify.accuracy(classifier,testing_set))*100)

classifier.show_most_informative_features(15)