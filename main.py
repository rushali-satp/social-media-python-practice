from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import User
from schemas import UserResponse
from user_API import router as user_router
app = FastAPI(title="User API")

app.include_router(user_router)




@app.get("/")
def home():
    return {"message": "FastAPI is running"}


@app.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.get("/bhumika")
def bhumika():
    return {"message": "My name is bhumika"}

