import random
import numpy as np


# These function pick a random output according to similarity and parse it accoedingly
def random_response(similarities, r):
    if np.all(
            (similarities <= 0.55)):  # if all are cosine similarities are belowe 0.65 then we don't have a close match
        return 'I am sorry I don\'t understand what you mean by that, could you please re-phrase it for me?'
    else:
        ans = [r[i] for i in np.argwhere(similarities > 0.55).flatten()]
        if len(ans) > 1:  # if more than one matches closely then pick a random one
            np.random.seed(2021)
            return random.choice(ans)
        else:
            return ans[0]


def recipe_random_response(similarities, name, response):
    if np.all((similarities <= 0.5)):  # if all are cosine similarities are belowe 0.55 then we don't have a
        # close match
        return None
    else:
        np.random.seed(2021)
        index = random.choice(np.argwhere(similarities > 0.5).flatten())
        name = name[index]
        recipe= response[index]

        text = '{}:'.format(name)
        text += '\nIngredients:'
        for i in recipe[0].replace('[', '').replace(']', '').replace('\"', '').split(','):
            text += '\n{}.'.format(i)
        text += '\nDirections:\n'
        for i in recipe[1].replace('[', '').replace(']', '').replace('\"', '').split(','):
            text += '{}'.format(i)
        return text
