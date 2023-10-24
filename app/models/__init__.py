from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
import user
import user_token
import shoes
import category

SQLALCHEMY_DATABASE_URL = "sqlite:///../db/shoe_shop.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False},
    echo=True
)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

database = Session()

