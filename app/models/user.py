from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, String, Boolean
from base import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    password = Column(String)
    token = relationship('UserToken', back_populates='parent')
    role = Column(String)
    status = Column(Boolean)
