from typing import List, Optional
from sqlalchemy.orm import Session

from models.user_model import Users as UserModel
from db.base import get_db

class UserService:
    
    def get_users(self, db: Session = get_db) -> List[UserModel]:
        return db.query(UserModel).all()

    def get_user(self, user_id: int, db: Session = get_db) -> Optional[UserModel]:
        return db.query(UserModel).filter(UserModel.id == user_id).first()

    def create_user(self, user: UserModel, db: Session = get_db) -> UserModel:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user