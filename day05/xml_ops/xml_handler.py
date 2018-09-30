# -*- coding:utf-8 -*-
# Author: Evan Mi
import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()
print(root.tag)
# 一个节点有tag、attrib、text三个值
# tag是标签的名字
# text是标签的内容
# attrib是标签属性的字典，通过字典的get('key')来获取对应的属性的值

# 直接for chile in parent 来遍历节点下的子节点
for child in root:
    print(child.tag, child.attrib)
    for elem in child:
        print(elem.tag, elem.text, elem.attrib)

# 只遍历year节点
for node in root.iter('year'):
    print(node.tag, node.text)
