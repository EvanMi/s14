# -*- coding:utf-8 -*-
# Author: Evan Mi
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func, and_, or_

engine = create_engine("mysql+pymysql://root:root@localhost/day12", encoding='utf-8', echo=True)
Base = declarative_base()  # 生成orm基类


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    billing_address_id = Column(Integer, ForeignKey('address.id'))
    shipping_address_id = Column(Integer, ForeignKey('address.id'))

    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))

    def __repr__(self):
        return self.street

Base.metadata.create_all(engine)