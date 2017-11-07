from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

EXAMPLE_TEXT = "This is a sample sentence, showing off the stop words filtration."

## print(sent_tokenize(EXAMPLE_TEXT))
word_tokens = word_tokenize(EXAMPLE_TEXT)

stop_words = set(stopwords.words('english'))

filtered_tokens = [w for w in word_tokens if not w in stop_words]

print(word_tokens)
print(filtered_tokens)