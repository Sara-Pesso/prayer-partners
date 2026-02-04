# Prayer Partners!

from math import *
import random
from directory import *

def random_prayer_partners(partners_list):
    # Make a copy to avoid modifying the original list in-place
    shuffled_list = partners_list[:] 
    random.shuffle(shuffled_list)

    # Group into pairs
    pairs = []
    for i in range(0, len(shuffled_list), 2):
        try:
            pairs.append([shuffled_list[i], shuffled_list[i+1]])
        except:
            pairs[-1].append(shuffled_list[-1])
    return pairs


random_pairs = random_prayer_partners(names)