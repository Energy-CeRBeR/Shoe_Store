from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, String, Boolean
from base import Base


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True)
    parent = relationship('Shoes', back_populates='category')
    name = Column(String)
    slug = Column(String)