#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Comtax():
    #コンストラクタ
    def __init__(self, price, tax):
        self.price = price
        self.tax = tax
    
    #メソッド
    def add_tax(self):
        print('商品の代金は「{price}円」です。'.format(price = self.price))
        print('税込「{plustax}円」です。'.format(plustax = self.price * self.tax))

        #intax = self.price * self.tax  -->> NG
        self.intax = self.price * self.tax

class Comtax2(Comtax):
    def parent(self):
        print('親クラスを継承しています。')
        super().add_tax()       #親のクラスのメソッドを呼び出す場合はsuper()

        #print(intax)  -->> NG
        print(self.intax)

if __name__ == "__main__":
    price = 10000
    tax = 1.08

    comtax = Comtax(price, tax)   #インスタンスを生成
    comtax.add_tax()              #インスタンス.メソッド名()

    comtax2 = Comtax2(price, tax) #インスタンスを生成, 親クラスの継承
    comtax2.parent()              #インスタンス.メソッド名()


'''
ref: https://qiita.com/Morio/items/0fe3abb58fcaff229f3d
'''