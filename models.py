from sqlalchemy.orm import Session
from database import Base, engine
from sqlalchemy import Column, Integer, String, Float

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    image_url = Column(String)

Base.metadata.create_all(bind=engine)

def get_products(db: Session):
    return db.query(Product).all()
