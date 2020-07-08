# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 19:09:58 2020

@author: vivek
"""

import sys
import collections

class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    
    def set_root(self, value):
        self.root = value
        
huffman_code=({})

def traverse_huffman_tree(node, code=''):
    if type(node) is str:
        return {node: code}
    
    left_node = node.get_left_child()
    right_node = node.get_right_child()
    
    huffman_code.update(traverse_huffman_tree(left_node, code + "0"))
    huffman_code.update(traverse_huffman_tree(right_node, code + "1"))
    return huffman_code

def huffman_encoding(data):
    tree=Tree()
    if data=='':
        return '-1',tree
    
    freq_dict=collections.OrderedDict()
    for char in data:
        freq_dict[char]=freq_dict.get(char,0)+1
    freq_dict={k: v for k, v in sorted(freq_dict.items(), key=lambda item: item[1])}
    
    if len(freq_dict)==1:
        char1, freq1 = freq_dict.popitem()
        root_node=Node()
        root_node.set_left_child(char1)
        root_node.set_right_child('')
    else:
        while len(freq_dict) > 1:
            char1, freq1 = freq_dict.popitem()
            char2, freq2 = freq_dict.popitem()
            new_node = Node()
            new_node.set_left_child(char1)
            new_node.set_right_child(char2)
            freq_dict[new_node]= freq1 + freq2
            freq_dict={k: v for k, v in sorted(freq_dict.items(), key=lambda item: item[1])}
            root_node = new_node
            
    tree.set_root(root_node)
    traverse_huffman_tree(root_node)
    encoded_string=''
    
    for char in data:
        encoded_string += huffman_code[char]
        
    return encoded_string,tree
  
def huffman_decoding(data,tree):
    decoded_string=''
    if data=='-1':
        return ''
    while len(data) > 0:
        node=tree.get_root()
        while type(node) is not str:
            if data[0] == "0" and node.has_left_child():
                data=data[1:]
                node=node.get_left_child()
            elif data[0] == "1" and node.has_right_child():
                data=data[1:]
                node=node.get_right_child()
        decoded_string += node
    return decoded_string

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Output: The size of the data is: 69
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Output: The content of the data is: The bird is the word
    
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output: The size of the encoded data is: 48
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Output: The content of the encoded data is: 10000001000000010000000000001000000001000000000100000000001000000000000000000010010000000000000010000001000000010000000000000001000001000000000100000000001
    
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output: The size of the decoded data is: 69
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    # Output: The content of the decoded data is: The bird is the word
    
    a_great_sentence = "hello world"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Output: The size of the data is: 60
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Output: The content of the data is: hello world
    
    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output: The size of the encoded data is: 32
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Output: The content of the encoded data is: 10100000000000000000000100100010000001000010000000000001
    
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output: The size of the decoded data is: 60
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    # Output: The content of the decoded data is: hello world
    
    a_great_sentence = "King and Queen"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Output: The size of the data is: 63
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Output: The content of the data is: King and Queen
    
    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output: The size of the encoded data is: 36
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Output: The content of the encoded data is: 10100000000000100000001000100000000000001000000010000010000001000000001000000001000000000
    
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output: The size of the decoded data is: 63
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    # Output: The content of the decoded data is: King and Queen
    
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Output: The size of the data is: 51
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Output: The content of the data is: 
    
    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output: The size of the encoded data is: 24
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Output: The content of the encoded data is: 0
    
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output: The size of the decoded data is: 16
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    # Output: The content of the decoded data is: 
    
    a_great_sentence = "aaaa"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Output: The size of the data is: 51
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # Output: The content of the data is: 
    
    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output: The size of the encoded data is: 24
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # Output: The content of the encoded data is: 0000
    
    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output: The size of the decoded data is: 53
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    # Output: The content of the decoded data is: aaaa
