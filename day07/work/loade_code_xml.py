# -*- coding:utf-8 -*-
# Author: Evan Mi
import xml.etree.ElementTree as ET
import os

code_dict = {
    'formatCode': 10,
    'healthcareFacilityTypeCode': 2,
    'practiceSettingCode': 3,
    'typeCode': 7,
    'classCode': 9,
    'confidentialityCode': 1
}

tree = ET.parse('XdsCodes.xml')
root = tree.getroot()
count = 100

with open('XdsCodes.sql', 'w') as f:
    for code_type in root:
        if code_type.tag == 'CodeType':
            num_val = code_dict.get(code_type.attrib['name'])
            if num_val is not None:
                for type_elem in code_type:
                    local_attribs = type_elem.attrib
                    sql = "INSERT INTO XDS_CODEVALUE VALUES(%d,%d,'%s','%s','%s');" % \
                          (count, num_val, local_attribs['code'], local_attribs['display'].replace("'", "''", 100),
                           local_attribs['codingScheme'])
                    count += 1
                    f.write(sql + os.linesep)
