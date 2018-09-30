# -*- coding:utf-8 -*-
# Author: Evan Mi
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper

metadata = MetaData()


user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(30)),
             Column('fullname', String(50)),
             Column('password', String(12))
             )


class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password


mapper(User, user)
