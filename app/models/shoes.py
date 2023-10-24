from sqlalchemy.orm import relationship
from sqlalchemy import Integer, Column, String, Boolean, ForeignKey
from base import Base


class Shoes(Base):
    __tablename__ = 'shoes'
    id = Column(Integer, primary_key=True, index=True)
    category = relationship('Category', back_populates='parent')
    category_id = Column(Integer, ForeignKey('category.id'))
    name = Column(String)
    slug = Column(String)
    image_path = Column(String)
    description = Column(String)
    price = Column(String)
    updated = Column(Boolean)
    available = Column(Boolean)
    created = Column(Boolean)