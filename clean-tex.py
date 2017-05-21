#!/usr/bin/python3

#IMPORT PACKAGES
import os as os #docs: https://docs.python.org/3.4/library/os.html
import argparse #docs: https://docs.python.org/3.4/library/argparse.html



#PARAMETERS
"""
These are the file extentions you want to delete.
Only add suffixes. No #file.tex prefixes. 
"""
rm_ls = [".aux", ".log", ".synctex.gz", ".out", ".dvi", "~"]






#FUNCTIONS
def clean_top_down(do_list, root_dir):
    count = 0
    for root, dirs, files in os.walk(root_dir): #get all files recursively from root down
        for file in files:
            for suffix in rm_ls:
                if file.endswith(suffix) and not file.startswith('.'): #skip hidden
                    if do_list:
                        print(os.path.join(root_dir, file)) #list
                    else:
                        os.remove(os.path.join(root, file)) #delete and count
                        count += 1
    return count


def clean_this_only(do_list, root_dir):
    count = 0
    files = os.listdir(root_dir) #get files in root directory
    for file in files:
        for suffix in rm_ls:
            if file.endswith(suffix) and not file.startswith('.'): #skip hidden
                if do_list:
                    print(os.path.join(root_dir, file)) #list
                else:
                    os.remove(os.path.join(root, file)) #delete and count
                    count += 1 
    return count


def clean(recursive, path, do_list):
    if recursive:
        count = clean_top_down(do_list, os.path.abspath(path))
    else:
        count = clean_this_only(do_list, os.path.abspath(path))

    print('\n' + str(count) + ' files deleted')







#MAIN
        
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='''
    Get rid of LaTeX/Emacs garbage in your directories.
    ''') #make an argument parser object

    #add definitions for arguments with help screen descriptions (see docs)
    parser.add_argument('-p',
                        '--path',
                        action='store',
                        metavar='',
                        default=os.curdir,
                        help='''
                        specify optional path to directory to clean 
                        (default is working directory)
                        ''')
    parser.add_argument('-r',
                        '--recursive',
                        action='store_true',
                        help='include this flag for recursive clean')
    parser.add_argument('-l',
                        '--list',
                        action='store_true',
                        help='include this flag to just list files')

    args = parser.parse_args() #parse the arguments passed to script
    clean(args.recursive, args.path, args.list)
