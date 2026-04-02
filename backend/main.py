from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine

from routes import categories, transactions, summary

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS (connect frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change later for security
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(categories.router, prefix="/categories")
app.include_router(transactions.router, prefix="/transactions")
app.include_router(summary.router, prefix="/summary")


@app.get("/")
def root():
    return {"message": "Finance Tracker API running"}