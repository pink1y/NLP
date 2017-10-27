# this program pick words as dimension for further analyse

import json
from pprint import pprint
import os
import math
import operator
from time import time
from pprint import pprint
from operator import add

# determine choosing method
# ---frequency control
freq = 100
# ---pos control
_pos = 'VB'
with open('word_bank_sorted.json', 'r') as _bank:
    all_words = json.load(_bank)
    
dim = {}

used = 0
for aW in all_words:

    # consider words only
    for char in aW[1]['word']: 
        if char.isalpha() != True:
            isWord = False
    if isWord == False:
        continue
        
    # consider the words with lower dfi
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
