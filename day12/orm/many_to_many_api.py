# -*- coding:utf-8 -*-
# Author: Evan Mi
import many_to_many
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=many_to_many.engine)  # 创建与数据库回话的session类
Session = Session_class()  # 实例化session类

book1 = many_to_many.Book(name='我们取', pub_date='2014-03-03')


Session.add_all([book1])

Session.commit()

"""
author_obj = Session.query(many_to_many.Author).filter(many_to_many.Author.name == 'Alex').first()
print(author_obj.books)
book_obj = Session.query(many_to_many.Book).filter(many_to_many.Book.id == 2).first()
print(book_obj.authors)
"""
Session.close()
