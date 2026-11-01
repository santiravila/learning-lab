from pydantic import BaseModel
from accounts.models import AccountType
from datetime import datetime


class AccountBase(BaseModel):
    account_type: AccountType
    balance: int
    password: str
    customer_id: int


class AccountCreate(AccountBase):
    pass


class AccountResponse(AccountBase):
    id: int
    created_at: datetime