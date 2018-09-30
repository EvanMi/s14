# -*- coding:utf-8 -*-
# Author: Evan
# import getpass

_username = "Evan"
_password = "qwerty"
username = input("username:")
# password = getpass.getpass("password:")
password = input("password:")

print(username, password)

if _username == username and _password == _password:
    print("Welcome user {name} login ...".format(name=username))
else:
    print("Invalid username %s or password %s!" % (username, password))
