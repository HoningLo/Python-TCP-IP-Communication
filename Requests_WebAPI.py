# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:27:18 2022

@author: M01
"""

import requests
import json


if __name__=='__main__':
    url = 'http://127.0.0.1:9527/items/'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    data = {"DeviceID": "____Enter_Your_DeviceID____"}
    response = requests.post(url, headers=headers, data=json.dumps(data), timeout=10)
    print(response.status_code, response.reason)
    print(response.headers)
    print(response.content)
    print(response.text)

