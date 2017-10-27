# this program pick words as dimension for further analyse

import json
import os
import math
import operator
from time import time

# determine choosing method
# ---frequency control
freq = 100
# ---pos control
_pos = 'VB'


with open('word_bank_sorted.json', 'r') as _bank:
    all_words = json.load(_bank)

# store choosed words
dim = {}

# index for choosed words
used = 0

for aW in all_words:

    # consider letters only
    for char in aW[1]['word']: 
        if char.isalpha() != True:
            isWord = False
    if isWord == False:
        continue
        
    # consider the words with lower freq
    if aW[1]['dfi'] > freq:
        continue
        
    # consider pos
    if not aW[1]['pos'].startswith(_pos):
        continue

    dim.update({
        aW[1]['word']: aW[1]
    })
    dim[aW[1]['word']].update({
        'index': used,
        'dfi_value': math.log10(304713/aW[1]['dfi'])
    })

    if used < 299:
        used += 1
    else:
        break

with open('word_bank_dim300.json', 'w') as dim300:
    json.dump(dim, dim300)
