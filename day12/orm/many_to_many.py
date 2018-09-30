# -*- coding:utf-8 -*-
# Author: Evan Mi
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:root@localhost/day12?charset=utf8", encoding='utf-8', echo=True)
Base = declarative_base()  # 生成orm基类

book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('id', Integer, primary_key=True),
                        Column('book_id', Integer, ForeignKey('books.id')),
                        Column('author_id', Integer, ForeignKey('authors.id')))


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author', secondary=book_m2m_author, backref='books')

    def __repr__(self):
        return self.name


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name


Base.metadata.create_all(engine)
