# -*- coding:utf-8 -*-
# Author: Evan Mi
import re
"""
'.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
'*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次
'{m}'   匹配前一个字符m次
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果['abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c
 
 
'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
'\Z'    匹配字符结尾，同$
'\d'    匹配数字0-9
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
'(?P<name>...)' 分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})",
"371481199306143242").groupdict("city")
 结果{'province': '3714', 'city': '81', 'birthday': '1993'}


最常用的匹配语法
re.match 从头开始匹配
re.search 匹配包含
re.findall 把所有匹配到的字符放到以列表中的元素返回

string="abcdefg  acbdgef  abcdgfe  cadbgfe"

regex=re.compile("((\w+)\s+\w+)")
print(regex.findall(string))
#输出：[('abcdefg  acbdgef', 'abcdefg'), ('abcdgfe  cadbgfe', 'abcdgfe')]
解释一下为什么这样的结果？很简单，当我们忽略括号，对整个字符串进行匹配的时候，要求是一到多个字母空格一到多个字母；
所以有两个结果'abcdefg  acbdgef'和'abcdgfe  cadbgfe'，但是我们是有括号的，所以给结果也加上括号，结果就变成了
'((abcdefg)  acbdgef)'和'((abcdgfe)  cadbgfe)',然而findall要返回括号里面的内容，而我们这里匹配了两次，每次有两个括号，
所以只好把每次的两个括号放在一个tuple中来区别哪此匹配的，tuple中的内容就是两个括号中的值；所以结果为：
[('abcdefg  acbdgef', 'abcdefg'), ('abcdgfe  cadbgfe', 'abcdgfe')]

regex1=re.compile("(\w+)\s+\w+")
print(regex1.findall(string))
#输出：['abcdefg', 'abcdgfe']
解释一下为什么这样的结果？很简单，当我们忽略括号，对整个字符串进行匹配的时候，要求是一到多个字母空格一到多个字母；
所以有两个结果'abcdefg  acbdgef'和'abcdgfe  cadbgfe'，但是我们是有括号的，所以给结果也加上括号，结果就变成了
'(abcdefg)  acbdgef'和'(abcdgfe)  cadbgfe',然而findall只返回括号里面的内容，所以结果是
['abcdefg','abcdgfe']


regex2=re.compile("\w+\s+\w+")
print(regex2.findall(string))
#输出：['abcdefg  acbdgef', 'abcdgfe  cadbgfe']
解释一下，这个没有括号了，两次匹配到的结果就是'abcdefg  acbdgef'和'abcdgfe  cadbgfe';没有括号，就在最外层默认加个括号，
变成了'(abcdefg  acbdgef)'和'(abcdgfe  cadbgfe)';所以结果是
['abcdefg  acbdgef', 'abcdgfe  cadbgfe'];

findall()返回的是括号所匹配到的结果（如regex1），多个括号就会返回多个括号分别匹配到的结果（如regex），
如果没有括号就返回就返回整条语句所匹配到的结果(如regex2)。所以在提取数据的时候就需要注意这个坑


print(re.sub('(.)\\1*', "2", test)) \1是代表第一个括号中的值
print(re.findall('(.)\\1*', test))
re.split 以匹配到的字符当做列表分隔符
re.sub      匹配字符并替换
"""