import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

ignore = ['hi', 'hello', 'hey', 'name', 'change', 'call', 'please', 'gordon']
# function to set the name of the user
def set_name(text):
    text = text.lower()
    text = [w.lower() for w in word_tokenize(text) if
            w not in stop_words and w not in string.punctuation and w not in ignore]  # filter text out
    if len(text) == 1:#if name is left return it
        return text[0].title()
    else: return 'invalid'#otherwise it is invalid
