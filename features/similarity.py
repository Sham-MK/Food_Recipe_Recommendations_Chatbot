from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from features.stemmer import stemmed_words_unfiltered, stemmed_words_filtered


# The functions here calculate the similrity between  query and set of questions or food titles and outputs the best match in the answers or recipes sets

def similarity_function(questions, query):
    query = [query]
    tfidf_vect = TfidfVectorizer(analyzer=stemmed_words_unfiltered)#load the TF-IDF vectorizer that does not filter stop words
    doc_tfidf_vect = tfidf_vect.fit_transform(questions) #fit and transform questions set
    query_tfidf_vect = tfidf_vect.transform(query) #transform query
    cosineSimilarities = cosine_similarity(doc_tfidf_vect, query_tfidf_vect).flatten()#get the matrix of cosine similarities between query and questions
    return cosineSimilarities


