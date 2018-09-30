# -*- coding:utf-8 -*-
# Author: Evan Mi
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, Enum
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, and_, or_

engine = create_engine("mysql+pymysql://root:root@localhost/day12", encoding='utf-8', echo=True)
Base = declarative_base()  # 生成orm基类


class User(Base):
        __tablename__ = 'user'
        id = Column(Integer, primary_key=True)
        name = Column(String(32))
        password = Column(String(64))

        def __repr__(self):
            return "<%s name:%s>" % (self.id, self.name)


class Student(Base):
        __tablename__ = 'student'
        stu_id = Column(Integer, primary_key=True)
        name = Column(String(32), nullable=False)
        register_date = Column(DATE, nullable=False)
        sex = Column(Enum('M', 'F'), nullable=False)

        def __repr__(self):
                return "<%s name:%s,regdate:%s,sex:%s>" % (self.stu_id, self.name, self.register_date, self.sex)

# Base.metadata.create_all(engine)


Session_class = sessionmaker(bind=engine)  # 创建与数据库回话的session类
Session = Session_class()  # 实例化session类
# user_obj = User(name='alex', password='alex3714')
# print(user_obj.name, user_obj.id)
# Session.add(user_obj)
# print(user_obj.name, user_obj.id)

# data = Session.query(User).filter_by(name='alex').all()
# data = Session.query(User).filter(User.id > 3).filter(User.name == 'xc').all()
#data = Session.query(User).filter(User.id > 3).filter(User.name == 'xc').first()
# data = Session.query(User).filter(User.name.in_(['what', 'alex'])).all()
# data = Session.query(User).filter(User.name.in_(['what', 'alex'])).count()
# print(data)
#data.name = 'what'
# print(Session.query(func.count(User.name), User.name).group_by(User.name).having(User.name=='alex').all())
# print(Session.query(User).filter(and_(User.id > 5,or_(User.name == 'alex', User.name =='what'))).all())

# s1 = Student(name='s2', register_date='2015-03-01', sex='M')
# Session.add(s1)
# res = Session.query(Student, User).filter(Student.stu_id == User.id).all()
# res = Session.query(User).join(Student, User.id == Student.stu_id).all()
# print(res)
Session.commit()
Session.close()
