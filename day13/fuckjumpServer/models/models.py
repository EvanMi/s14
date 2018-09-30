# -*- coding:utf-8 -*-
# Author: Evan Mi
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, Enum, ForeignKey, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()  # 生成orm基类


user_m2m_bindhost = Table('user_m2m_bindhost', Base.metadata,
                          Column('id', Integer, primary_key=True, autoincrement=True),
                          Column('userprofile_id', Integer, ForeignKey('user_profile.id')),
                          Column('bindhost_id', Integer, ForeignKey('bind_host.id')))

class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True)
    ip = Column(String(64), unique=True)
    port = Column(Integer, default=22)

    def __repr__(self):
        return self.hostname


class HostGroup(Base):
    __tablename__ = 'host_group'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True)

    def __repr__(self):
        return self.name


class RemoteUser(Base):
    __tablename__ = 'remote_user'
    __table_args__ = (UniqueConstraint('auth_type', 'username', 'password', name='au_us_pa_unique'),)
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32))
    password = Column(String(128))
    auth_type = Column(Enum('PASS', 'Key'))

    def __repr__(self):
        return self.username


class BindHost(Base):
    """host_ip group romote_user"""
    __tablename__ = 'bind_host'
    __table_args__ = (UniqueConstraint('host_id', 'group_id', 'rmoteuser_id', name='host_group_remoteuser_unique'),)
    id = Column(Integer, primary_key=True, autoincrement=True)
    host_id = Column(Integer, ForeignKey('host.id'))
    group_id = Column(Integer, ForeignKey('host_group.id'))
    rmoteuser_id = Column(Integer, ForeignKey('remote_user.id'))

    host = relationship('Host', backref='bindhosts')
    group = relationship('HostGroup', backref='bindhosts')
    remoteuser = relationship('RemoteUser', backref='bindhosts')

    def __repr__(self):
        return '<%s -- %s -- %s>' % (self.host.ip, self.remoteuser.username, self.group.name)


class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32), unique=True)
    password = Column(String(128))
    bind_hosts = relationship('BindHost', secondary=user_m2m_bindhost, backref='user_profiles')

    def __repr__(self):
        return self.username


class AuditLog(Base):
    pass
