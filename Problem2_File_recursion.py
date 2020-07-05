# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:22:17 2020

@author: vivek
"""

import os
# Let us print the files in the directory in which you are running this script

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.isdir(path):
        return 'Invalid Directory'
    
    file_list=[]
    
    for file in os.listdir(path):
        if file.endswith(suffix):
            file_list.append(file)
        
        sub_dir=os.path.join(path,file)
        
        if os.path.isdir(sub_dir):
            file_list+=find_files(suffix,sub_dir)
                
    return file_list


# Let us check if this file is indeed a file!
print(find_files('.c', './testdir'))

