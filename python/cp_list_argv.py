#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def main():

    import sys
    import os

    args = sys.argv
    argc = len(args)

    if argc != 2: # file & args
        print('args is more or less')
        return False
    filename = args[1]
    
    current_path = os.getcwd()
    path_to_file = current_path + '/' + filename
    f = open(path_to_file, 'r')
    datalist = f.readlines()
    f.close()
    
    for data in datalist:
        list_row_name = data.rstrip('\n')
        print(list_row_name)
        
        ####write code below#####

if __name__ == "__main__":
    main()

'''
./main_argv.py filename.txt
cp_list_argv.txt
text1
text2
text3
'''


