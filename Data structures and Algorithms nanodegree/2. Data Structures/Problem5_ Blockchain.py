# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 21:38:02 2020

@author: vivek
"""

import hashlib
import time

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def __str__(self):
        return ('Timestamp: {}\nData: {}\nPrevious Hash: {}\nHash: {}'.format(self.timestamp, self.data, self.previous_hash, self.hash))
    

class Blockchain:
    def __init__(self):
        self.current_block=None
        
    def set_block(self,text):
        timestamp=time.gmtime()
        self.current_block=Block(timestamp, text, self.current_block)
    
    def get_block(self):
        return self.current_block
        
blockchain=Blockchain()
blockchain.set_block(5)
blockchain.set_block('abc')
blockchain.set_block('gh')
print(blockchain.get_block())
"""
Output:
Timestamp: time.struct_time(tm_year=2020, tm_mon=7, tm_mday=5, tm_hour=19, tm_min=58, tm_sec=37, tm_wday=6, tm_yday=187, tm_isdst=0)
Data: gh
Previous Hash: Timestamp: time.struct_time(tm_year=2020, tm_mon=7, tm_mday=5, tm_hour=19, tm_min=58, tm_sec=37, tm_wday=6, tm_yday=187, tm_isdst=0)
Data: abc
Previous Hash: Timestamp: time.struct_time(tm_year=2020, tm_mon=7, tm_mday=5, tm_hour=19, tm_min=58, tm_sec=37, tm_wday=6, tm_yday=187, tm_isdst=0)
Data: 5
Previous Hash: None
Hash: a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
Hash: a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
Hash: a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
"""