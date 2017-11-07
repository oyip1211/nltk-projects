from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

ps = PorterStemmer()

EXAMPLE_TEXT = "My name is Oliver Yip. I'm a pen, I'm an apply. Oh - Pineapple pen."

word_tokens = word_tokenize(EXAMPLE_TEXT)

for w in word_tokens:
	print(ps.stem(w))