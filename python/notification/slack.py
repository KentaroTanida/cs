#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

def main():

    # Incoming WebHooks
    URL='https://hooks.slack.com/'
    # 送信内容
    TEXT='write text here'
    # user name
    USERNAME='slack username'
    # Icon
    ICON = ':bowtie:'

    # post
    post_json = {
        'text': TEXT,
        'username': USERNAME,
        'icon_emoji': ICON
    }
   
    requests.post(URL, data = json.dumps(post_json))


if __name__ == "__main__":
    main()



'''
Icon list
https://qiita.com/yamadashy/items/ae673f2bae8f1525b6af
'''


