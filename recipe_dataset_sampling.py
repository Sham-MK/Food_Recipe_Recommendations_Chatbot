import random
import pandas
import yaml
#this function samples a smaller random set of the dataset and saves it to a yml file
with open('RecipeNLG_dataset.csv', encoding='utf-8') as file:
    n = 2231143 #number of records in file
    s = 5001 #desired sample size
    skip = sorted(random.sample(range(n),n-s+1))
    df = pandas.read_csv(file, skiprows=skip)
    # drop unwated columns
    cols = [0,4,5,6]
    df = df.drop(df.columns[cols], axis=1).values.tolist()#convert panda data frame to list
with open('corpora/recipes.yml', 'w') as outfile:
    yaml.dump(df, outfile, default_flow_style=False)#write to a yaml file