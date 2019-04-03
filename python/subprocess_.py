#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

def main():

    cmd = 'ls -la'
    res = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    res.wait()
    print(res)

def main2():

    cmd = ['ls -la']
    res = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    res.wait()
    print(res.communicate()[0].decode("utf8"))




if __name__ == "__main__":
    main()
    main2()

'''
call
check_call
check_output
Popen
'''

'''
改行コードを削除
.rstrip('\n')
'''

