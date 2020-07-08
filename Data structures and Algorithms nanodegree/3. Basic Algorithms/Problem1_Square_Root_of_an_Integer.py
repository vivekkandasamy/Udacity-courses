# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:04:03 2020

@author: vivek
"""

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number<0:
        return None
    if number==0:
        return 0
    
    lower_limit=1
    upper_limit=number
    
    while True:
        middle=(lower_limit+upper_limit)//2
        if middle==lower_limit or middle*middle==number:
            return middle
        if middle*middle<number:
            lower_limit=middle
        elif middle*middle>number:
            upper_limit=middle

print ("Pass" if  (3 == sqrt(9)) else "Fail")
#output: Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")
#output: Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")
#output: Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")
#output: Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")
#output: Pass