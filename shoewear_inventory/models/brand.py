from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from shoewear_inventory.models.base import Base, SessionLocal


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    products = relationship("Product", back_populates="brand")

    @classmethod
    def create(cls, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Brand name must be a non-empty string.")
        db = SessionLocal()
        existing = db.query(cls).filter_by(name=name).first()
        if existing:
            raise ValueError("Brand already exists.")
        brand = cls(name=name)
        db.add(brand)
        db.commit()
        db.refresh(brand)
        return brand

    @classmethod
    def delete(cls, brand_id):
        db = SessionLocal()
        brand = db.query(cls).get(brand_id)
        if not brand:
            raise ValueError("Brand not found.")
        db.delete(brand)
        db.commit()

    @classmethod
    def get_all(cls):
        db = SessionLocal()
        return db.query(cls).all()

    @classmethod
    def find_by_id(cls, brand_id):
        db = SessionLocal()
        brand = db.query(cls).get(brand_id)
        if not brand:
            raise ValueError("Brand not found.")
        return brand

    @classmethod
    def find_by_name(cls, name):
        db = SessionLocal()
        return db.query(cls).filter(cls.name.ilike(f"%{name}%")).all()