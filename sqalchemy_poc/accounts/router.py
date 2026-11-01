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

DbSession = Annotated[Session, Depends(get_db_session)]
def get_service_dependency(
    db: DbSession, 
    customer_repo: CustomerRepository,
    account_repo: AccountRepository      
):
    return AccountService(customer_repo(db), account_repo(db))

ServiceDep = Annotated[AccountService, Depends(get_service_dependency)]

@router.post("", response_model=AccountResponse)
def create_account(
    account_payload: AccountCreate,
    service: ServiceDep
) -> AccountResponse:
    account = service.add_account(account_payload)
    return AccountResponse.model_validate(account)
