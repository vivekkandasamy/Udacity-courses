# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:42:49 2020

@author: vivek
"""
def pivot_point(input_list):
    """
    Find the pivot point by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search
    Returns:
       int: Index of the pivot point
    """
    
    lower_limit=0
    upper_limit=len(input_list)-1
    while True:
        middle=(lower_limit+upper_limit)//2
        if input_list[middle]>input_list[lower_limit]:
            lower_limit=middle
        elif input_list[middle]<input_list[upper_limit]:
            upper_limit=middle
        else:
            break;
    return middle

def binary_search(input_list, number, lower_limit, upper_limit):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int), lower_limit(int), upper_limit(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
     
    if upper_limit>=lower_limit:
        middle=(lower_limit+upper_limit)//2
         
        if input_list[middle] == number: 
            return middle 
        
        elif input_list[middle] > number: 
            return binary_search(input_list, number, lower_limit, middle-1)
  
        else: 
            return binary_search(input_list, number, middle+1, upper_limit)
        
    else:
        return -1
     
        
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list==[]:
        return -1
    
    if len(input_list)==1:
        if input_list[0]==number:
            return 0
        return -1
    
    middle=pivot_point(input_list)
    
    if input_list[0]>number:
        lower_limit=middle+1
        upper_limit=len(input_list)-1
    else:
        lower_limit=0
        upper_limit=middle
    
    index=binary_search(input_list, number, lower_limit, upper_limit)
    return index



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Output: Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Output: Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Output: Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# Output: Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Output: Pass