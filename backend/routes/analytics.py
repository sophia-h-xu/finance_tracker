# routes/analytics.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import SessionLocal
from models import Transaction, Category

router = APIRouter(prefix="/analytics")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/breakdown/{user_id}")
def get_breakdown(user_id: int, db: Session = Depends(get_db)):
    results = (
        db.query(Category.name, func.sum(Transaction.amount))
        .join(Transaction)
        .filter(Transaction.user_id == user_id)
        .group_by(Category.name)
        .all()
    )

    return [{"category": r[0], "total": r[1]} for r in results]