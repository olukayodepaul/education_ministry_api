from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.account_opening_service import AccountOpeningService

def open_account(db: Session = Depends(get_db)):
    return AccountOpeningService(db=db)
