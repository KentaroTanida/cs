#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

def main():
    items = ['name', 'phone', 'address']
    df = pd.DataFrame([], columns=items)
    print(df)

    sample = [['taro', '090-xxxx-xxxx', 'Tokyo'], ['jiro', '090-xxxx-xxxx', 'Okinawa'], ['saburo', '090-xxxx-xxxx', 'Hokkaido']]

    for i in range(len(sample)):
        print(sample[i])
        series = pd.Series(sample[i], index = df.columns)
        print(series)
        df = df.append(series, ignore_index = True)

    print(df)

    output_to_csv(df)

def output_to_csv(data):
    data.to_csv('./pandas_no_ki.csv')


if __name__ == "__main__":
    main()





#ref: https://qiita.com/567000/items/d8a29bb7404f68d90dd4


