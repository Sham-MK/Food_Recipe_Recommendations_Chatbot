from nltk import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer


# these functions are used for Tf_idf vectorization of doc with stemming and filtering of stop words

def stemmed_words_filtered(doc):
    p_stemmer = PorterStemmer()
    analyzer = TfidfVectorizer(use_idf=True,lowercase=True, sublinear_tf=True, decode_error="ignore",
                               stop_words=stopwords.words('english')).build_analyzer()
    return (p_stemmer.stem(w) for w in analyzer(doc))


def stemmed_words_unfiltered(doc):
    p_stemmer = PorterStemmer()
    analyzer = TfidfVectorizer(use_idf=True, sublinear_tf=True, lowercase=True, decode_error="ignore").build_analyzer()
    return (p_stemmer.stem(w) for w in analyzer(doc))
