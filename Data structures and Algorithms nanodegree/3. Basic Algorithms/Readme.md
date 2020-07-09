# Data structures and Algorithms Nanodegree

# 2. Data Structures

# Project Explanation
Explanation of the different project submodules

## Problem 1: Square Root of an Integer
Square root of a positve number always lies between 0 and number itself.

For the __Square root__ problem, i used __binary search algorithm__ to find the floor value of square root of given number.

### Time and Space complexity

The time complexity of binary search algorithm is O(log(n)). The space complexity is O(1).

## Problem 2: Search in a Rotated Sorted Array
Two __binary search algorithms__ are used to search the index of a given number in array.

The first algorithm is used to find the __pivot point__ and the second algorithm is used to find the __index__.

### Time and Space complexity
The time complexity for both binary search algorithm is O(log(n)) and their sum will also be same. The space complexity is O(1)

## Project 3
A challenging problem that took a considerable time to understand the algorithm and solve the problem.

Following steps are involved in solving the problem.

1. A string is taken and frequency of each character is determined and stored as key/value pair
2. Build a Huffmann tree.
3. Encode the text in compression form
4. Decode the data using the Hufman tree and compressed text

The time complexity is given by O(nlogn) and the space complexity is given by O(n)

## Project 4
The code checks if the user is on the given group. If not, check the subgroup and its subgroup

Since the depth of sub groups is not predefined, recursion model is used.

The time complexity is O(n), where n is the total number of users and groups to be searched. The space complexity is o(1) used to search the algorithm.

## Project 5
The code creates an hashble block chain with timestamp and reference to previous hashes

The get and set methods are used to add new blocks and read the existing blocks

The time and space complexity is o(1), since the function adds new entry in constant time and constant space.

## Project 6

This code is used to create union and intersection of two Linkedlist. Additional function to_list to convert a given linked list into list are written under class Linkedlist.

First the union(or intersection) list of both input lists are created using set function. Later a new linkedlist is created using the union(or intersection) list

The time complexity is O(n*m), where n and m are the number of entries in list 1 and list 2 respectively. The space complexity is o(1).
