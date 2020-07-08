# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:38:04 2020

@author: vivek
"""

def merge_sort(values): 
  
    if len(values)>1: 
        m = len(values)//2
        left = values[:m] 
        right = values[m:] 
        left = merge_sort(left) 
        right = merge_sort(right) 
  
        values =[] 
  
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                values.append(left[0]) 
                left.pop(0) 
            else: 
                values.append(right[0]) 
                right.pop(0) 
  
        for i in left: 
            values.append(i) 
        for i in right: 
            values.append(i) 
                  
    return values

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list==[]:
        return[-1,-1]
    sorted_list=merge_sort(input_list)
    number1=''
    number2=''
    for i in range(len(sorted_list)):
        if i%2==1:
            number1=str(sorted_list[i])+number1
        else:
            number2=str(sorted_list[i])+number2
    return [int(number1), int(number2)]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
# Output: Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# Output: Pass
test_function([[], [-1,-1]])
# Output: Pass