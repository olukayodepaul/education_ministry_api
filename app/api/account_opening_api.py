from fastapi import APIRouter, Depends

from app.models.user import User
from app.services.account_opening_service import AccountOpeningService
from typing import List
from app.di.dependencies import open_account

router = APIRouter()

@router.get("/opening/{id}", response_model=List[User])
def get_users(id: int, account: AccountOpeningService = Depends(open_account)):
    return account.open_accounts(id)