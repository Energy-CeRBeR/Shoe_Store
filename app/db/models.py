from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker, relationship
from sqlalchemy import Column, Integer, String,Boolean, ForeignKey


SQLALCHEMY_DATABASE_URL = "sqlite:///./shoe_shop.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False},
    echo=True
)

Base = declarative_base()


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


class UserToken(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True, index=True)
    parent = relationship('User', back_populates='token')
    parent_id = Column(Integer, ForeignKey('user.id'))
    token = Column(String)


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True)
    parent = relationship('Shoes', back_populates='category')
    name = Column(String)
    slug = Column(String)


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


Base.metadata.create_all(bind=engine)

Session = sessionmaker(autoflush=True, bind=engine)

database = Session()