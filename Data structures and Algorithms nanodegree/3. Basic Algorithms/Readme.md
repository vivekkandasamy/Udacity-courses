# Data structures and Algorithms Nanodegree

# 3. Basic Algorithms

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
The time complexity for both binary search algorithm is O(log(n)) and their sum will also be same. The space complexity is O(1).

## Problem 3: Rearrange Array Digits

In this problem elements of an array are rearranged so as to form two number such that their sum is maximum. For sorting the elements of the array merge sort algorithm is used.

### Time and Space complexity
Merge sort algorithm has a time complexity of o(nlog(n)) and a space complexity of o(n)

## Problem 4: Dutch National Flag Problem
A list with elements 0,1,2 is sorted with a single traversal.

### Time and Space complexity
The space complexity is o(1) and time complexity is o(n)

## Problem 5: Autocomplete with Tries
In this method Tries method is used to add words to a dcitionary. Later these dictionary of words are used to provide auto suggestions of words based on first few characters that the user enters. For this recursive functions are used.

### Time and Space complexity
Since Trie uses for loops with calls for suffixes for each character, the time complexity is O(nxm), where n is the number of words and m is the number of charcters in each word. The space complexity is also O(n), because of the recursive function. 

## Problem 6: Unsorted Integer Array

In this problem the max and min values in a given list is found. The algorithm compares every elements in the list and find the minimum and maximum values.

### Time and Space complexity
Since the algoritm searches each and every element in the list the time complexity is o(n) and space complexity is o(1).

## Problem 7: Request Routing in a Web Server with a Trie
The problem is similar to problem with exceptions like file handler. Here paths are added into the trie. Later if we search a path, trie returns the corresponding handler or not found handler.

### Time and Space complexity
Usage of for loops to find paths on Trie node results in a time complexity of O(nxm), where n is the number of paths and m is the number of charcters in each path. The space complexity will be O(n).
