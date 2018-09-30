# -*- coding:utf-8 -*-
# Author: Evan Mi

_root = {'l1_1': {'l2_1': ['l3_01', 'l3_02'], 'l2_2': ['l3_03', 'l3_04']},
         'l1_2': {'l2_3': ['l3_05', 'l3_06'], 'l2_4': ['l3_07', 'l3_08']},
         'l1_3': {'l2_5': ['l3_09', 'l3_10'], 'l2_6': ['l3_11', 'l3_12']}
         }


curr_node = None

for key in _root:
    print(key)

while True:
    node = input("please type in the node you want to deep,b to get back ,q to exit:")
    if '' == node:
        print('input can not be empty!')
    elif 'b' == node:
        curr_node = None
        for key in _root:
            print(key)
    elif 'q' == node:
        print('bye!')
        break
    elif curr_node is None and node in _root.keys():
        curr_node = _root[node]
        for key in curr_node:
            print(key)
    elif type(curr_node) == dict and node in curr_node.keys():
            curr_node = curr_node[node]
            for key in curr_node:
                print(key)
    elif type(curr_node) != dict:
        print('this is the last level already')
    else:
        print('Invalid input!')
