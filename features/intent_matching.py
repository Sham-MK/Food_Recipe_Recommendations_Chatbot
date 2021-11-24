import os
import pickle
# function to predict intent of query
def intent_predictor(query):
    # load the pre-trained classiication model
    parent = os.getcwd()
    path = parent + '/model/tf_vectorizer.pickle'
    with open(path, "rb") as f:
        tfidf_vect = pickle.load(f)
    query = tfidf_vect.transform([query])
    # load the pre-fitted tfidf vectorized
    path = parent + '/model/trained_model.pickle'
    with open(path, "rb") as f:
        classifier = pickle.load(f)
        category = classifier.predict(query)
    return category[0]
