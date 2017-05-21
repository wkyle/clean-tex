#!/usr/bin/python3

#import packages
import os as os



#parameters
"""
These are the file extentions you want to delete.
Only add suffixes. No #file.tex prefixes. 
"""
rm_ls = [".aux", ".log", ".synctex.gz", ".out", ".dvi", "~"]



#functions
def clean_top_down(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            for suffix in rm_ls:
                if file.endswith(suffix):
                    os.remove(os.path.join(root, file))

def clean_this_only(root_dir):
    files = 3
    for file in files:
        for suffix in rm_ls:
            if file.endswith(suffix):
                os.remove(os.path.join(root, file))







if __name__ == "__main__":

    if here down:
        clean_top_down(os.curdir)
    if there down:
        clean_top_down(os.path.abspath(path_to_directory))
    if here only:
        clean_this_only(os.curdir)
    if there only:
        clean_this_only()
