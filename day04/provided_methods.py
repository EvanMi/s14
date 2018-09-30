# -*- coding:utf-8 -*-
# Author: Evan Mi
import functools
# 取绝对值
print('abs:', abs(-1))
# 如果一个可迭代对象的所有元素都为真，返回true ;空也返回真
print('all:', all([1, 0, -3]))
# 有一个为真就全为真
print('any:', any([1, 0, -1]))
# 变成可打印的字符串格式
print('ascii:', ascii([1, 2]))
# 把整数转换成2进制
print('bin:', bin(2))
# 判断真假
print('bool:', bool(1 == 2))
# 创建一个可修改的byte数组
print('bytearray:', bytearray('Evan', encoding='utf-8'))
# 创建一个不可修改的byte数组
print('bytes', bytes('Evan', encoding='utf-8'))
# 是否是否可调用（也就是是不是一个类或函数 --后面能不能加括号）
print('callable:', callable([]))
# 把Unicode转换为对应的字符
print('chr:', chr(97))
# 把字符转换为unicode
print('ord:', ord('我'))
# 把字符串转为python obj
print('compile:', compile('for i in range(10):print(i)', '', 'exec'))
# 返回一个复数
print('complex:', complex(2, 3))
# 生成一个字典
print('dict:', dict())
# 查看有什么方法可用
print('dir:', dir({}))
# 返回两个数相除的商和余数
print('divmod:', divmod(5, 3))
# 加载一个字符串为python的数据可是
print('eval:', eval('{"name":"Evan","age":12}'))
# 执行一段命令或代码
print('exec:')
exec('for i in range(10): print(i)')
# 给一个列表加上前缀下标
print('enumerate')
for x, y in enumerate(['a', 'b', 'c']):
    print(x, y)
# 过滤
print('filter:')
f_res = filter(lambda n: n > 5, range(10))
for x in f_res:
    print(x)
# 给可迭代对象中的每个元素做一个操作，返回操作后的可迭代对象
print('map:')
map_res = map(lambda xx: xx**2, [1, 2, 3])
for mx in map_res:
    print(mx)
# reduce((((0+1)+2)+3)+4)
print('reduce:')
re_res = functools.reduce(lambda rx, ry: rx+ry, range(5))
print(re_res)
# 字符串转化为浮点数
print('float:', float('123.2'))
# 创建不可变列表
print('frozenset:', frozenset([1, 2, 3, 4, 5]))
# 返回这个python文件中的所有定义的变量的key-value
print('globals:', globals())
# 字符串的hash值
print('hash:', hash('Evan'))
# 转为16进制字符串
print('hex:', hex(22))
# 返回内存地址
print('id:', id('232323'))
# 获取局部变量
print('locals:', locals())
# 最大值
print('max: ', max(1, 4, 6))
# 最小值
print('min: ', min(2, 5, 6))
# 转8进制字符串
print('oct:', oct(12))
# 幂运算
print('pow:', pow(2, 3))
# 转字符串
print('repr:', repr(2323))
# 保留n位小数 4舍5入
print("round:", round(23.3353, 2))
# 排序
mmap = {6: 2, 3: 3, 2: 1}
print('sorted')
print(mmap)
print(sorted(mmap.items()))
print(sorted(mmap.items(), key=lambda kx: kx[1]))
# 查看数据类型
print('type:', type(1))
# zip
zres = zip(['a', 'b', 'c', 'd'], [1, 2, 3])
for zs in zres:
    print(zs)

