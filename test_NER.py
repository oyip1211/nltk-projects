import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sentence_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sentence_tokenizer.tokenize(sample_text)

try:
	for s in tokenized:
		words = nltk.word_tokenize(s)
		tagged = nltk.pos_tag(words)
		namedEntity = nltk.ne_chunk(tagged,binary=True)
		namedEntity.draw()
except Exception as e:
	print(str(e))
