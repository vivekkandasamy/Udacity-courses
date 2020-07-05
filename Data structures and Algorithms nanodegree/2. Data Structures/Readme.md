# Data structures and Algorithms Nanodegree

# Project Explanation
Explanation of the different project submodules

## Project 1
For the __LRU_Cache__ problem, i used ordereddict since popitem() can be used to function as FIFO(First In First Out) with Ordereddict().

### Time and Space complexity
The time complexity of get() is O(1), because there is no loops. The space complexity of get() is O(1), due to the fact that only one variable is allocated

The time complexity of set() is O(1), because there is no loops. The space complexity of set() is O(n) because the complete dictionary has to be gone through to set values

## Project 2
Here __python os__ module is used to search the files inside the directories. 

Since there can be any number of sub directories, recursion model is used to cover maximum sub directories.
