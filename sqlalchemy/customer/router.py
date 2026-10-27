from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from infrastructure.database import get_db_session
from sqlalchemy.orm import Session
from .schema import CustomerCreate, CustomerResponse
from .repository import CustomerRepository


router = APIRouter(prefix="/customers", tags=["customers"])


@router.post("", response_model=CustomerResponse)
def create_customer(
    customer_payload: CustomerCreate,
    db: Annotated[Session, Depends(get_db_session)]
    ) -> CustomerResponse:
    repo = CustomerRepository(db)
    db_customer = repo.save_customer(customer_payload)
    return CustomerResponse.model_validate(db_customer)

"""
@router.get("{customer_id}")
def get_customer(
    customer_id: int,
    repo: Annotated[CustomerRepository, Depends(repository_dependency)]
    ) -> CustomerResponse:
    try:
        customer = repo.get_customer(customer_id)
        customer_dto = CustomerMapper.domain_to_dto(customer)
    except ValueError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(err)
        )
    else:
        return customer_dto
"""