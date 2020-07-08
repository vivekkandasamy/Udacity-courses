# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 00:10:49 2020

@author: vivek
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints==[]:
        return None
    minimum=ints[0]
    maximum=ints[0]
    for i in ints:
        if i>maximum:
            maximum=i
        if i<minimum:
            minimum=i
    return (minimum,maximum)


## Example Test Case of Ten Integers
import random

l1 = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l1)

print ("Pass" if ((0, 9) == get_min_max(l1)) else "Fail")
#Output: Pass

l2=[]
print ("Pass" if (None == get_min_max(l2)) else "Fail")
#Output: Pass

l3 = [i for i in range(-35, 60)]  # a list containing 0 - 9
random.shuffle(l3)

print ("Pass" if ((-35, 59) == get_min_max(l3)) else "Fail")
#Output: Pass