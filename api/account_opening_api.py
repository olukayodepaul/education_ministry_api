from fastapi import APIRouter, Depends

from models.user import User
from services.account_opening_service import AccountOpeningService
from typing import List
from di.dependencies import open_account

router = APIRouter()

@router.get("/opening/{id}", response_model=List[User])
def get_users(id: int, account: AccountOpeningService = Depends(open_account)):
    return account.open_accounts(id)