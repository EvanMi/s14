# -*- coding:utf-8 -*-
# Author: Evan Mi
import json
with open('test.txt', 'r') as f:
    data = json.loads(f.read())
    print(data)
    print(data.get('age'))
