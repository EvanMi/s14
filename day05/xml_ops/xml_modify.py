# -*- coding:utf-8 -*-
# Author: Evan Mi
import xml.etree.ElementTree as ET

tree = ET.parse('test.xml')
root = tree.getroot()

# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)   # 修改内容
    node.set("updated", "yes")  # 修改属性

tree.write('tt.xml')


# 删除
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)
tree.write('tt1.xml')
