from nltk.corpus import wordnet

"""
syns = wordnet.synsets("beautiful")
print(syns[0].name())
print(syns[0].lemmas()[0].name())
print(syns[0].definition())
print(syns[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("bad"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
        	antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))
"""

w1 = wordnet.synset('clock.n.01')
w2 = wordnet.synset('watch.n.01')
print(w1.wup_similarity(w2))