from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, String, Boolean, ForeignKey
from base import Base


class UserToken(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True, index=True)
    parent = relationship('User', back_populates='token')
    parent_id = Column(Integer, ForeignKey('user.id'))
    token = Column(String)