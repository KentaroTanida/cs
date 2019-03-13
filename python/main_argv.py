#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def personal_info(name, phone, address):
    print('{name}\'s phone number:{phone} & Address:{address}'.format(name = name, phone = phone, address = address))

def main():

    import sys

    args = sys.argv
    argc = len(args)

    if argc != 4: # file & args
        print('args is more or less')
        return False

    name = args[1]
    phone = args[2]
    address = args[3]

    personal_info(name, phone, address)
    
    

if __name__ == "__main__":
    main()


'''
./main_argv.py taro 090-xxxx-xxxx Tokyo Japan
./main_argv.py taro 090-xxxx-xxxx Tokyo
'''


