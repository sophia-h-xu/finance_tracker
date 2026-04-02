from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/pie")
def pie_summary(db: Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    transactions = db.query(models.Transaction).all()

    result = {}

    for t in transactions:
        category = next((c for c in categories if c.id == t.category_id), None)
        if category:
            result[category.name] = result.get(category.name, 0) + t.amount

    total = sum(result.values())

    return {
        "breakdown": result,
        "total": total
    }


@router.get("/trends")
def trends(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).all()

    trends = {}

    for t in transactions:
        key = t.date.strftime("%Y-%m")
        trends[key] = trends.get(key, 0) + t.amount

    return trends