from functools import reduce
from random import randrange
from itertools import repeat
import numpy as np
import pandas as pd



#carga del archivo
l = list(map(lambda l: (l.strip()).split(','),
             open('ratings.txt', 'r').readlines()))

# construccion del training: 2 de cada 3

print (enumerate(l))


train = np.zeros((203,9742))
train = list(map(lambda x: x[1],
filter(lambda v: v[0] %3 != 0, enumerate(l))))


#print(train)
