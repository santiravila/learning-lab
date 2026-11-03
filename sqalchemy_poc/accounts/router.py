from fastapi import APIRouter, Depends, HTTPException, status
from infrastructure.database import get_db_session
from typing import Annotated
from sqlalchemy.orm import Session
from customers.repository import CustomerRepository
from .schema import AccountCreate, AccountResponse
from .repository import AccountRepository
from .service import AccountService


router = APIRouter(
    prefix="/accounts", 
    tags=["accounts"]
)

DBSession = Annotated[Session, Depends(get_db_session)]
def get_service_dependency(db: DBSession):
    customer_repo = CustomerRepository(db)
    account_repo = AccountRepository(db)
    return AccountService(customer_repo, account_repo)

ServiceDep = Annotated[AccountService, Depends(get_service_dependency)]

@router.post("", response_model=AccountResponse)
def create_account(
    account_payload: AccountCreate,
    service: ServiceDep
) -> AccountResponse:
    account = service.add_account(account_payload)
    return AccountResponse.model_validate(account)

@router.get("{account_id}", response_model=AccountResponse)
def get_account(
    account_id: int,
    service: ServiceDep
) -> AccountResponse:
    account = service.find_account(account_id)
    return AccountResponse.model_validate(account)
