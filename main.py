#!/usr/bin/python3
import time
from random import shuffle
from algolib.search import binary_search
from algolib.sorting import selection_sort
from algolib.rand import RandGen

first_array = [1, 3, 5, 7, 9, 10, 11, 12, 14]

randgen = RandGen(time.time())
print(binary_search(first_array, 10)) # => 5
print(binary_search(first_array, 100)) # => None
print(randgen.randint(1, 10))
print(randgen.randfloat(1.0, 10.0))
print(randgen.randchoice(first_array))
print(randgen.randshuffle(first_array))
