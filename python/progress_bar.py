#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tqdm import tqdm
import time

def main():
    for i in tqdm(range(100)):
        time.sleep(0.02)


#print(__name__)


if __name__ == "__main__":
    main()



