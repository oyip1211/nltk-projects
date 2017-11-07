from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import gutenberg

sample = gutenberg.raw("bible-kjv.txt")

pst = PunktSentenceTokenizer()
token = pst.tokenize(sample)

for i in range(5):
	print(token[i+6])

