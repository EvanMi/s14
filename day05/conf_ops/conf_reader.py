# -*- coding:utf-8 -*-
# Author: Evan Mi
import configparser

config = configparser.ConfigParser()
# 加载文件
config.read('example.ini')

# 读取所有的section
print(config.sections())
# 读取DEFAULT配置信息
print(config.defaults())
# 读取某个信息
print(config[config.default_section]['ForwardX11'])
