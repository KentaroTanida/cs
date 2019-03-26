#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/v1/target', methods=['POST'])
def new_machine():
    #print(request.data.decode('utf-8'))
    data = request.data.decode('utf-8')
    data = json.loads(data)
    print(name['fuga'])

    return 'THX'

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5050)



'''
#test command
curl -H "Content-type: application/json" -X POST -d '{"name": "fuga"}' 0.0.0.0:5050/v1/target
'''


'''
#Flask並列処理について
https://qiita.com/5zm/items/251be97d2800bf67b1c6
'''


