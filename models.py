import enum
from datetime import datetime

from sqlalchemy import Integer, String, Column, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Worker(Base):
    __tablename__ = 'worker'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    phone_number = Column(String(20), nullable=False)
    email = Column(String(40), nullable=False)
    address = Column(String(25), nullable=False)
    password = Column(String(25), nullable=False)

    calls = relationship('Call', back_populates='worker')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    phone_number = Column(String(20), nullable=False)
    email = Column(String(40), nullable=False)
    address = Column(String(25), nullable=False)

    calls = relationship('Call', back_populates='user')


class Call(Base):
    __tablename__ = 'call'

    id = Column(Integer, primary_key=True)
    call_date = Column(DateTime, default=datetime.utcnow())
    duration = Column(Integer, nullable=False)
    worker_id = Column(Integer, ForeignKey('worker.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    status = Column(Enum('accepted', 'failed', name='status_enum', create_type=False))

    worker = relationship('Worker', back_populates='calls')
    user = relationship('User', back_populates='calls')
