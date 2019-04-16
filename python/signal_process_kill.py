#!/usr/bin/python3
# coding: UTF-8


import signal
import os
import time

loop = True

def receive_signal(signum, stack):
    print('Received:', signum)
    global loop
    loop = False

signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

print('My PID is:', os.getpid())



while loop:
    print('Waiting...')
    time.sleep(3)



'''
プロセス停止
kill -SIGUSR1 < PID >

nohup /home/user/sample.py > /tmp/nohup.log &
'''
