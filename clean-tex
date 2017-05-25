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
                if file.endswith(suffix) and not file.startswith('.') and not '/.' in root: #skip hidden
                    if do_list:
                        print(os.path.join(root, file)) #list
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
                    os.remove(os.path.join(root_dir, file)) #delete and count
                count += 1
    return count


def clean(recursive, path, do_list):
    if recursive:
        count = clean_top_down(do_list, os.path.abspath(path))
    else:
        count = clean_this_only(do_list, os.path.abspath(path))

    return count



#MAIN
        
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='''
    Get rid of LaTeX/Emacs garbage in your directories.
    Removes .aux, .log, .out, .synctex.gz, and *~ files
    ''') #make an argument parser object

    #add definitions for arguments with help screen descriptions (see docs)
    parser.add_argument('path',
                        nargs='?',
                        default=os.getcwd(),
                        help='indicate directory to clean (default to working dir)')
    parser.add_argument('-r',
                        '--recursive',
                        action='store_true',
                        help='include this flag for recursive clean')

    args = parser.parse_args() #parse the arguments passed to script
    count = clean(args.recursive, args.path, True)
    do_clean = input("Do you want to delete " + str(count) + " files? (Y/n)")
    if do_clean == "Y":
        clean(args.recursive, args.path, False)
        print("Deleted " + str(count) + " files")

