# This script pre-processes the small talk dataset and splits it into messages and responses lists
import os
import yaml


# this function process the data and outputs pairs of messages and responses
def pre_process(category):
    data_list = []
    m = []
    r = []
    filepath = 'D:\\Users\\shamm\\PycharmProjects\\CW1' + '/corpora' + os.sep + category + '.yml'
    if category.lower() == 'recipes':  # parsing of recipes dataset is different
        with open(filepath, encoding='utf8', errors='ignore', mode='r') as file:
            for i in yaml.load(file, Loader=yaml.FullLoader):
                data_list.append({i[0]: i[1:3]})  # turn the recipes names to keys
    else:
        # loop through every file and store the list of conversations in conversation_list
        with open(filepath, encoding='utf8', errors='ignore', mode='r') as file:
            for i in yaml.load(file, Loader=yaml.FullLoader)["conversations"]:
                data_list.append({i[0]: i[1]})
        # separate the keys from values
    for i in data_list:
        m += [*i]
        r += [*i.values()]
    return m, r

