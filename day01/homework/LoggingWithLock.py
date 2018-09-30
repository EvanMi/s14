# -*- coding:utf-8 -*-
# Author: Evan Mi

user_name = input("username:")
pass_word = input("password:")

if '' == user_name or '' == pass_word:
    print("username and password can't be empty!")
    exit(0)

file_object = open('E:\\pythondata\\day01\\user_pass.txt')
fileLock = open('E:\\pythondata\\day01\\locked_user.txt', 'r+')
try:
    count = 0
    for line in fileLock:
        if line == '{_user_name} \n'.format(_user_name=user_name):
            count += 1

    if count >= 3:
        print("your account is locked!")
        exit(0)

    for line in file_object:
        my_tuple = line.split()
        if len(my_tuple) != 2:
            continue

        if my_tuple[0] == user_name and my_tuple[1] == pass_word:
            print("Welcome {_user_name} ...".format(_user_name=user_name))
            break
        elif my_tuple[0] == user_name and my_tuple[1] != pass_word:
            print("password error!")
            fileLock.write("{_user_name} \n".format(_user_name=user_name))
            break
    else:
        print("Invalid user name!")
finally:
    file_object.close()
    fileLock.close()
