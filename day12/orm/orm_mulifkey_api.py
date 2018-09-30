# -*- coding:utf-8 -*-
# Author: Evan Mi
import orm_mutifkey
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_mutifkey.engine)  # 创建与数据库回话的session类
Session = Session_class()  # 实例化session类
"""
addr1 = orm_mutifkey.Address(street='tiantongyuan', city="cangping", state='beijing')
addr2 = orm_mutifkey.Address(street='wudaokou', city="cangping", state='beijing')
addr3 = orm_mutifkey.Address(street='yanjiao', city="langfang", state='hebei')

Session.add_all([addr1, addr2, addr3])

p1 = orm_mutifkey.Customer(name="Alex", billing_address=addr1, shipping_address=addr2)
p2 = orm_mutifkey.Customer(name="Jack", billing_address=addr3, shipping_address=addr3)

Session.add_all([p1, p2])
"""
obj = Session.query(orm_mutifkey.Customer).filter(orm_mutifkey.Customer.name == 'Alex').first()
print(obj.name, obj.billing_address, obj.shipping_address)

Session.commit()
Session.close()
