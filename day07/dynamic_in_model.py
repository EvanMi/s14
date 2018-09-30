# -*- coding:utf-8 -*-
# Author: Evan Mi
# from work import  test
import importlib
mod_name = 'work.test'
# __import__(mod_name)
my_mod = importlib.import_module(mod_name)
print(my_mod)
xx = my_mod.C()
print(xx.name)