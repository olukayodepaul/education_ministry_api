from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models.user_model import User as UserModel
from services.user_service import UserService
from db.base import get_db
from typing import List

router = APIRouter()
user_service = UserService()

@router.get("/users", response_model=List[UserModel])
def get_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)

@router.get("/users/{user_id}", response_model=UserModel)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=UserModel)
def create_user(user: UserModel, db: Session = Depends(get_db)):
    return user_service.create_user(user, db)
