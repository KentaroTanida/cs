#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

def main():
    items = ['name', 'phone', ' address']
    d = pd.DataFrame([], columns=items)
    print(d)

    sample = [['taro', '090-xxxx-xxxx', 'Tokyo'], ['jiro', '090-xxxx-xxxx', 'Okinawa'], ['saburo', '090-xxxx-xxxx', 'Hokkaido']]

    for i in range(len(sample)):
        print(sample[i])
        series = pd.Series(sample[i], index = d.columns)
        d = d.append(series, ignore_index = True)

    print(d)

    output_to_csv(d)

def output_to_csv(data):
    data.to_csv('./pandas_no_ki.csv')


if __name__ == "__main__":
    main()

