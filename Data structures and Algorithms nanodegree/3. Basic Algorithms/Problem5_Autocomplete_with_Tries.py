# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 21:04:12 2020

@author: vivek
"""

"""
Building a Trie in Python

Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
* A `Trie` class that contains the root node (empty string)
* A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

Give it a try by implementing the `TrieNode` and `Trie` classes below!
"""
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children={}
        self.is_word=False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char]=TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        results=[]
        if self.is_word:
            results.append(suffix)    
        for char in self.children:
            results.extend(self.children[char].suffixes(suffix=suffix+char))
        return results
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root=TrieNode()
        
    def insert(self, word):
        ## Add a word to the Trie
        current_node=self.root
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node=current_node.children[char]
        current_node.is_word=True
                

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node=self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node=current_node.children[char]
        return current_node
    

    
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

f('an')
"""
Output:
t
thology
tagonist
tonym
"""

f('sa')
"""
Output:
sa not found
"""

f('0123')
"""
0123 not found
"""

f('t')
"""
Output:
rie
rigger
rigonometry
ripod
"""