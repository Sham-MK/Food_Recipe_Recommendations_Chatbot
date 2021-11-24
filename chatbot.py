from features.identity_management import set_name
from features.intent_matching import intent_predictor
from features.preprocess import pre_process
from features.response_parse import recipe_random_response, random_response
from features.similarity import similarity_function

#preprocess the recipes dataset first as it takes time to load
names, recipes = pre_process('recipes')
# name prompt and intro
print('If you wish to exit, type Bye.')
print('Gordon: Hello, my name is Gordon, your assisting chef on demand. What is your name?')
n = input('User : ')
# set the name variable
name = set_name(n)
while name.lower() == 'invalid':
    n = input('Please enter your name: ')
    name = set_name(n)
print('Gordon: Hi ' + name + ', How can I help you?')
# main program loop
flag = True
while flag:
    query = input(name + ': ')
    # check if user enterd Bye for termination
    if query.lower() == 'bye':
        print('Gordon: This is Gordon signing off. Thank you for chatting with me ' + name + ', take care <3')
        flag = False
    else:
        # otherwise get the intent of the query
        intent = intent_predictor(query)
        if intent.lower() == 'recipes':  # if the intent is to get a recipe then preprocess our recipe data, get the closest match and print the parsed output
            print('Please hold on a minute while I check my database for the closest recipe for your craving. :)')
            simlarities = similarity_function(names, query)
            text = recipe_random_response(simlarities,names, recipes)
            if text != None:
                print('Gordon: ' + text)
                print('Gordon: Was that helpful?')
                a = input(name+ ': ')
                if 'yes' in a.lower(): print('I am happy to help')
                elif 'no' in a.lower():
                    print('I am sorry, please hold on a minute while I check my database for another recipe for your craving. :)')
                    text = recipe_random_response(simlarities, names, recipes)
                    print('Gordon: ' + text)
                else:
                    print('Gordon: I am sorry I don\'t understand what you mean by that')
            else: print('Gordon: I am sorry I don\'t seem to have this recipe in my database, could you please re-phrase it for me, ' \
               'or ask for something else? ')
        elif intent.lower() == 'naming':  # if the intent is to manage identity
            m, r = pre_process(intent)
            similarities = similarity_function(m, query)
            result = random_response(similarities,r)
            if result.lower() == 'set':  # check if it is to get or set (change) the name
                name = set_name(query)
                while name.lower() == 'invalid':
                    n = input('Please enter your name: ')
                    name = set_name(n)
                print('Gordon: I shall call you {} from now on'.format(name))
            else:
                print('Gordon: Your name is {}'.format(name))
        else:#otherwise it is small talk
            m, r = pre_process(intent)
            similarities = similarity_function(m, query)
            result = random_response(similarities, r)
            print('Gordon: ' + result)
