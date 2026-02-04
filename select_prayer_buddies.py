# Prayer Partners!

from math import *
import random
from directory import *

def random_prayer_partners(file):
    names, name_to_email = get_directory(file)
    # Make a copy to avoid modifying the original list in-place
    shuffled_list = names[:] 
    random.shuffle(shuffled_list)

    # Group into pairs
    pairs = []
    for i in range(0, len(shuffled_list), 2):
        try:
            pairs.append([shuffled_list[i], shuffled_list[i+1]])
        except:
            pairs[-1].append(shuffled_list[-1])
    return pairs, names, name_to_email
