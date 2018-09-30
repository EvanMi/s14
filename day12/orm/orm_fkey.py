# -*- coding:utf-8 -*-
# Author: Evan Mi
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func, and_, or_

engine = create_engine("mysql+pymysql://root:root@localhost/day12", encoding='utf-8', echo=True)
Base = declarative_base()  # 生成orm基类


class Student1(Base):
    __tablename__ = 'student1'
    stu_id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)
    sex = Column(Enum('M', 'F'), nullable=False)

    def __repr__(self):
        return "<%s name:%s,regdate:%s,sex:%s>" % (self.stu_id, self.name, self.register_date, self.sex)


class StudyRecord1(Base):
    __tablename__ = 'study_record1'
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer, ForeignKey("student1.stu_id"))
    student = relationship("Student1", backref="my_study_record")

    def __repr__(self):
        return "<%s day:%s,status:%s,stu_id:%s>" % (self.id, self.day, self.status, self.stu_id)


#Base.metadata.create_all(engine)
Session_class = sessionmaker(bind=engine)  # 创建与数据库回话的session类
Session = Session_class()  # 实例化session类
"""
s1 = Student1(name='s1', register_date='2018-03-28', sex='F')
s2 = Student1(name='s2', register_date='2018-03-28', sex='F')
s3 = Student1(name='s3', register_date='2018-03-28', sex='F')
s4 = Student1(name='s4', register_date='2018-03-28', sex='F')
s5 = Student1(name='s5', register_date='2018-03-28', sex='F')


study_obj1 = StudyRecord1(day=1, status='YES', stu_id=1)
study_obj2 = StudyRecord1(day=2, status='NO', stu_id=1)
study_obj3 = StudyRecord1(day=3, status='YES', stu_id=1)
study_obj4 = StudyRecord1(day=1, status='YES', stu_id=2)

Session.add_all([s1, s2, s3, s4, s5, study_obj1, study_obj2, study_obj3, study_obj4])
"""

# res = Session.query(func.count(StudyRecord1.id)).join(Student1).filter(Student1.name == 's1').all()
stu_obj = Session.query(Student1).filter(Student1.name == 's1').first()
res = stu_obj.my_study_record
print(res)
Session.commit()
Session.close()


