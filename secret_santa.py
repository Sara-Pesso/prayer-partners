# Secret Santa!


from math import *
import random

names =['Gene','Kristen','Tristan','Tessa','Perrin','Beth','Cullen','Sara','Liam','Carolyn',
'Owen','Juliana','Phineas','Theodora','Josiah']

spouses = {'Gene':'Kristen',
'Tristan':'Tessa',
'Perrin':'Beth',
'Cullen':'Sara',
'Liam':'Carolyn',
'Owen':'Juliana'}

def flip_dict_entries(dict):
    flipped_dict = {value: key for key, value in dict.items()}
    merged_dict = dict | flipped_dict
    return merged_dict


def secret_santa_generator(names, spouses):
    spouses = flip_dict_entries(spouses)

    n = len(names)
    tries = 0
    while True:
        random_order = random.sample(range(0,n), n)
        pairings = {names[i]: names[random_order[i]] for i in range(0, n)}
        spouse_check = True
        for giver, receiver in pairings.items():
            if giver == receiver or spouses.get(giver) == receiver:
                spouse_check = False
                tries += 1
                break
        if spouse_check:
            pairings_str = []
            for key, value in pairings.items():
                pairings_str.append(f"{key} DREW {value}")
            return pairings_str

# print(secret_santa_generator(names, spouses))