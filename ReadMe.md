# Recipe Recommendation Chatbot
A dynamic chatbot that engages in shallow conversations and recommends recipes according to user input.

##How To Run
Simply execute the chatbot.py file (found it the root directory of the project) on your command line interface or desired IDE.

###Remarks
* The model and vectorizer pickle file were written with python 3.9, if you run a different version of python, it is advisable to run the model training file again to avoid warnings. The model training script can be found at root/features/model_training.py.
* All the feature functions are found in th features directory.
* The corpora datasets can be found in the corpora directory.
* The model and vectorizer pickle files can be found in the model directory.
* The sampling script is in the root directory and is called recipe_dataset_sampling.py, and the URL of the original dataset is:https://www.kaggle.com/paultimothymooney/recipenlg