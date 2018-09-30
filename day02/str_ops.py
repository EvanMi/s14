# -*- coding:utf-8 -*-
# Author: Evan Mi

name = "my name is alex"

print(name.capitalize())  # 首字母大写
print(name.count("a"))  # 统计整个字符中a的个数
print('aaaaa'.count("a", 0, len('aaaaa')-1))  # 前闭后开
print(name.center(50, "-"))  # 打印50个字符，name在中间，不够的用-来填充
print(name.endswith("ex"))  # 打印name是否以ex结尾
print(name.expandtabs(tabsize=30))  # 扩展\t为多少个空格
print(name.find("name"))  # 找到name中最左边的‘name’的开始字母的下标
print(name[name.find("name"):name.find("name")+len("name")])

name1 = "my name is {_name}"
print(name1.format_map({"_name": "Evan"}))  # 用一个map来格式化

print(name.isalnum())  # 当只有字母或数字的时候返回True
print('12asd'.isalpha())  # 是否是纯英文字符
print("2".isdecimal())  # 是否是十进制 方法检查字符串是否只包含十进制字符前面加 u
print("1".isdigit())  # 是否是整数
print("1A".isidentifier())  # 判断是不是一个合法的表示符 也就是是不是一个合法的变量名
print("3333.3".isnumeric())  # 判断是不是只包含数字
print("aa".isspace())  # 判断是不是空格
print("My Name Is ".istitle())  # 每个首字母大写
print('My Name Is '.isprintable())  # 是否可以打印 tty file,drive file
print("NN".isupper())  # 是否是大写
print("ll".islower())  # 是否是小写
print(",".join(['1', '2', '3']))  # 直接join字符串列表
print(name.ljust(50, '*'))  # 把name放在最左面，写50个字符，不够的用*填充
print(name.rjust(50, '$'))  # 把那么放在最有面，写50个字符，不够的用$填充
print('NAME'.lower())  # 全部转换为小写
print('name'.upper())   # 全部转换为大写
print('Alex\n'.rstrip())    # 去掉右边的回车和换行
print('Alex\n'.lstrip())    # 去掉左边的回车和换行
print('\nAlex\n'.strip())  # 去掉两边的回车和空格


p = str.maketrans('abcdef', '123456')  # 制作一个翻译对照，一对一的
print('alex li'.translate(p))   # 翻译某个字符串


print('alex li'.replace('l', 'L'))  # 替换 默认全部替换
print('alex li'.replace('l', 'L', 1))   # 替换几个
print('alex li'.rfind('l'))     # 找到alex li 中最又边的‘name’的开始字母的下标
print('alex li'.split('l'))  # 字符串分割为数组 默认为空格
print('123\n232323'.splitlines())   # 按行分割为数组
print('123'.startswith('1'))    # 以1开始
print('Alex Li'.swapcase())     # 大小写互换
print('alex li'.title())    # 转换为标题
print('lex li'.zfill(50))   # 写50个字符，提供的字符不足50个，前面补零
