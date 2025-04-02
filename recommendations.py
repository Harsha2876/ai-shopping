from sqlalchemy.orm import Session
import random
import models

def recommend_products(db: Session, product_id: int):
    all_products = db.query(models.Product).all()
    return random.sample(all_products, min(3, len(all_products)))  # Return 3 random products
