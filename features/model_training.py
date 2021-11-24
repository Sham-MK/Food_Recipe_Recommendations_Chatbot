import os
import pickle
import yaml
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from features.stemmer import stemmed_words_filtered

# initialize training data and label sets
data = []
labels = []

# parse through every file in the dataset folder
path = os.path.dirname(os.getcwd()) + '/corpora'
for file in os.listdir(path):
    category = file.split('.')[0]  # get the label name from the file name
    filepath = path + os.sep + file
    if category.lower() == 'recipes':  # the parsing of recipes dataset is different
        recipes_list = []
        with open(filepath, encoding='utf8', errors='ignore', mode='r') as file:
            for i in yaml.load(file, Loader=yaml.FullLoader):  # load the data and append it to lists
                data.append(i[0])
                labels.append(category)
            # This is simply to dilute the dataset with some question statements as all the data is just food recipe names
            asking_for_recipes = ['Give me the recipe for', 'Can you tell me the recipe for', 'How to cook',
                                  'what is the recipe for', 'How to make', 'How to bake', 'get me a recipe',
                                  'salty', 'something sweet', 'sour', 'hot food', 'some dessert']
            asking_for_recipes_labels = [category] * 12
            data.extend(asking_for_recipes)
            labels.extend(asking_for_recipes_labels)
    else:
        with open(filepath, encoding='utf8', errors='ignore', mode='r') as file:
            conversation_list = []
            for i in yaml.load(file, Loader=yaml.FullLoader)["conversations"]:  # get the conversations section of the file
                data.append(i[0])
                labels.append(category)

# This code was used to analyse the classes in the dataset
# label, count = np.unique(labels, return_counts=True)
# print(dict(zip(label,count)))

# X_train, X_test, y_train, y_test = train_test_split(data, labels, stratify=labels, test_size=0.20, random_state=42)
tfidf_vect = TfidfVectorizer(analyzer=stemmed_words_filtered)  # initialize te TF-ID vctorizer with our predifind
# function which takes care of stemming and stop words
X_train_tf = tfidf_vect.fit_transform(data)
classifier = RandomForestClassifier(random_state=0).fit(X_train_tf,
                                                        labels)  # use the random forest classifier to learn

#this code was used to determin the best classifier on the dataset
# X_new_tfidf = tfidf_vect.transform(X_test)
# predicted = classifier.predict(X_new_tfidf)
# print(accuracy_score(y_test, predicted))
# print(classification_report(y_test, predicted))

# save the model and vectorizer
with open("../model/trained_model.pickle", "wb") as f:
    pickle.dump(classifier, f)
with open("../model/tf_vectorizer.pickle", "wb") as f:
    pickle.dump(tfidf_vect, f)
