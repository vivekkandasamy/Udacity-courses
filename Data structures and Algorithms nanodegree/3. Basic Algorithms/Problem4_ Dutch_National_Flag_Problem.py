# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:06:19 2020

@author: vivek
"""

def sort1(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # arr=[0,0,0]
    # for i in input_list:
    #     arr[i]=arr[i]+1
    # return arr[0]*[0]+arr[1]*[1]+arr[2]*[2]
    cp_input_list=input_list[:]
    curr_index=0
    end_index=len(cp_input_list)
    
    while curr_index<end_index:
        
        if cp_input_list[curr_index]==0:
            cp_input_list=[cp_input_list.pop(curr_index)]+cp_input_list
            curr_index+=1
            
        elif cp_input_list[curr_index]==2:
            cp_input_list=cp_input_list+[cp_input_list.pop(curr_index)]
            end_index-=1
            
        else:
            curr_index+=1
            
    return cp_input_list

def test_function(test_case):
    sorted_array = sort1(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# Output: Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# Output: Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# Output: Pass
test_function([])
# Output: Pass
