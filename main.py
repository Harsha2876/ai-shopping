from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from database import SessionLocal, init_db
import models, recommendations

app = FastAPI()
templates = Jinja2Templates(directory="templates")

init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    products = models.get_products(db)
    return templates.TemplateResponse("index.html", {"request": request, "products": products})

@app.get("/product/{product_id}")
def product_detail(product_id: int, request: Request, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    recommendations_list = recommendations.recommend_products(db, product_id)
    return templates.TemplateResponse("product.html", {"request": request, "product": product, "recommendations": recommendations_list})
