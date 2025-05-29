
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///shoewear.db")

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def init_db():
    from shoewear_inventory.models.brand import Brand
    from shoewear_inventory.models.product import Product
    Base.metadata.create_all(bind=engine)