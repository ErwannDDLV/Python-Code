# using python3 in terminal
# test

import argparse
import glob
import os
import stat
import sys
import time

from datetime import datetime 

def file_list(path):
    if os.path.isdir(path):
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)) and not file.startswith('.'):
                print(file)
    else:
        for file in glob.glob(path + '*.*', recursive=True):
            print(os.path.basename(file))
            
def files_list_mode(path):
    total = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) and not file.startswith('.'):
            total.append(file)
    print('total : %s' % len(total))

    for file in os.listdir(path):
        pathname = os.path.join(path, file)
        permissions = stat.filemode(os.stat(pathname).st_mode)
        created_date = datetime.fromtimestamp(os.stat(pathname).st_ctime)

        if os.path.isfile(pathname) and not file.startswith('.'):
            print("%s %s %s" % (
                permissions,
                created_date,
                file)
            )

def main():

    parser = argparse.ArgumentParser(
        prog="test for Brice",
        usage='%(prog)s [options]',
        formatter_class=lambda prog: argparse.HelpFormatter(prog, width=100, max_help_position=30), 
        description='List files in directory and return the result.'
    )
        
    parser.add_argument("path", help='path to your folder')
    parser.add_argument('-l', "--files_list_mode", action = 'store_const', const = files_list_mode, help='List files from your directory with mode and creation date')

    args = parser.parse_args()

    if args.files_list_mode: files_list_mode(args.path)
    elif args.path: file_list(args.path)

if __name__ == '__main__':
    main()
