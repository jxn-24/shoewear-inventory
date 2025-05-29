from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from shoewear_inventory.models.base import Base, SessionLocal
from shoewear_inventory.models.brand import Brand


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    image_url = Column(String(255))
    description = Column(String(500))
    price = Column(Float, nullable=False)

    brand_id = Column(Integer, ForeignKey('brands.id'))
    brand = relationship("Brand", back_populates="products")

    @classmethod
    def create(cls, name, image_url, description, price, brand_id):
        db = SessionLocal()
        brand = db.query(Brand).get(brand_id)
        if not brand:
            raise ValueError("Brand ID does not exist.")

        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Product name must be a non-empty string.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")

        product = cls(
            name=name,
            image_url=image_url,
            description=description,
            price=float(price),
            brand_id=brand_id
        )
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @classmethod
    def delete(cls, product_id):
        db = SessionLocal()
        product = db.query(cls).get(product_id)
        if not product:
            raise ValueError("Product not found.")
        db.delete(product)
        db.commit()

    @classmethod
    def get_all(cls):
        db = SessionLocal()
        return db.query(cls).all()

    @classmethod
    def find_by_id(cls, product_id):
        db = SessionLocal()
        product = db.query(cls).get(product_id)
        if not product:
            raise ValueError("Product not found.")
        return product

    @classmethod
    def find_by_attribute(cls, attribute, value):
        db = SessionLocal()
        filters = {
            'name': cls.name.ilike(f"%{value}%"),
            'price': cls.price >= float(value),
            'brand': cls.brand.has(Brand.name.ilike(f"%{value}%"))
        }
        query = db.query(cls).filter(filters.get(attribute, None))
        return query.all()