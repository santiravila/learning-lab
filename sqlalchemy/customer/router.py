from fastapi import APIRouter, Depends, HTTPException, status
from .schema import CustomerCreate, CustomerResponse
from .mappers.customer_mapper import CustomerMapper
from .repository import CustomerRepository
from typing import Annotated

def repository_dependency() -> CustomerRepository:
    repo = CustomerRepository()
    return repo


router = APIRouter(prefix="/customers", tags=["customers"])


@router.post("")
def create_customer(
    customer_payload: CustomerCreate,
    repo: Annotated[CustomerRepository, Depends(repository_dependency)]
    ) -> CustomerResponse:

    domain = CustomerMapper.dto_to_domain(customer_payload)
    domain_answer = repo.save_customer(domain)
    return CustomerMapper.domain_to_dto(domain_answer)


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