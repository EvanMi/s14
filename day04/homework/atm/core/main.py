# -*- coding:utf-8 -*-
# Author: Evan Mi
import sys
import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACCOUNT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\account\\%s.txt'
LOG_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\logs\\logs.txt'


def atm_auth(account_type):
    def out_wrapper(fun):
        def wrapper(*args, **kwargs):
            username = input('username:')
            password = input('password:')
            if account_type == 'admin' and username != 'admin':
                print('you are not admin')
                print_log('%s tried to login as admin' % username)
                return
            try:
                with open(ACCOUNT_DIR % username, 'r') as f:
                    account_info = json.load(f)
                    if account_info.get('password') == password:
                        print_log('%s has successfully login into the system' % username)
                        if username != 'admin':
                            kwargs['username'] = username
                        return fun(*args, **kwargs)
                    else:
                        print('invalid password')
                        print_log('%s has failed to login into the system because of an error password' % username)
            except FileNotFoundError:
                print('account do not exits!')
                print_log('%s do not exist in system, but tried to login into the system' % username)
        return wrapper
    return out_wrapper


def print_log(info):
    with open(LOG_DIR, 'a') as f:
        f.write(info + '\n')


@atm_auth(account_type='admin')
def admin_add_user(username, password, money=1000000):
    if os.path.exists(ACCOUNT_DIR % username):
        print('user account already exist')
        print_log('admin tried to add account %s,which already exist' % username)
    else:
        with open(ACCOUNT_DIR % username, 'w') as f:
            account_info = {'username': username, 'password': password, 'account': money}
            json.dump(account_info, f)
            print_log('admin add a account into the system,named %s' % username)


@atm_auth(account_type='admin')
def admin_del_user(username):
    if not os.path.exists(ACCOUNT_DIR % username):
        print('user do not exist')
        print_log('admin tried to delete a not exist account %s' % username)
        return
    in_word = input('the deleted file can not be find back,sure to delete? y/n')
    if in_word == 'y':
        os.remove(ACCOUNT_DIR % username)
        os.replace()
        print('delete operation success')
        print_log('admin has successfully deleted a account named %s' % username)
    else:
        print('user canceled the delete operation')
        print_log('admin has canceled deleted a account named %s' % username)


@atm_auth(account_type='admin')
def admin_lst_user():
    res = os.listdir(BASE_DIR+'\\account\\')
    print('the customers are listed at below'.center(200, '*'))
    for name in res:
        prefix_name = name.split('.')[0]
        if not prefix_name == 'admin':
            print(prefix_name)
    print(('total nums is : %d' % (len(res)-1)).center(200, '*'))
    print_log('admin has listed all users in system')


def user_show_balance(user_info):
    print('your account balance is %s !' % user_info.get('account'))


@atm_auth(account_type='user')
def user_get_money(username):
        f = open(ACCOUNT_DIR % username, 'r')
        user_info = json.load(f)
        user_show_balance(user_info)
        wanted_money = float(input('please input the money you want to get:'))
        if user_do_pay(username, wanted_money, lambda x: x + x * 0.05):
            print('you have get %s money,the charge is %s' % (wanted_money, wanted_money * 0.05))
            print_log('%s have get %s money' % (username, wanted_money))
        else:
            print_log('you do not have enough money')


@atm_auth(account_type='user')
def user_pay_money(username):
    wanted_money = float(input('please input the money you want to get:'))
    if user_do_pay(username, wanted_money, lambda x: x):
        print_log('%s have pay %s money' % (username, wanted_money))
        return 'successfully paid %s' % wanted_money
    else:
        return 'you do not have enough money'


def user_do_pay(username, in_money, fun):
    f = open(ACCOUNT_DIR % username, 'r')
    user_info = json.load(f)
    user_money = user_info.get('account')
    pay_money = fun(in_money)
    if pay_money > user_money:
        return False
    user_info['account'] = user_money - pay_money
    f.close()
    with open(ACCOUNT_DIR % username, 'w') as ft:
        json.dump(user_info, ft)
    return True


user_get_money()
