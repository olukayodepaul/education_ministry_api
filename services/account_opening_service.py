from typing import List

from models.user import User
from sqlalchemy.orm import Session
from db import account_opening_schema as AccountOpeningSchema

class AccountOpeningService:
    
    def __init__(self, db: Session):
        self.db = db
    
    def open_accounts(self, id: int) -> List[User]:
      deleted_post = self.db.query(AccountOpeningSchema.AccountOpeningSchema).all()
      return deleted_post