#!/usr/bin/env python


import os


def get_all_files(path):
    files=[]
    rooted_files=[]
    for file in os.listdir(path):
        if os.path.isdir(path+"/"+file):
            print(path+"/"+file)
            rooted_files=rooted_files+get_all_files(path+"/"+file)
        files.append(file)

    files=files+rooted_files
    return files

print(get_all_files("/dev"))


