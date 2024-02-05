from typing import List

from app.models.user import User
from sqlalchemy.orm import Session
from app.db import account_opening_schema 

class AccountOpeningService:
    
    def __init__(self, db: Session):
        self.db = db
    
    def open_accounts(self, id: int) -> List[User]:
      deleted_post = self.db.query(account_opening_schema.AccountOpeningSchema).all()
      return deleted_post