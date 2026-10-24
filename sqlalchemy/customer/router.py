from fastapi import APIRouter
from .schema import CustomerCreate, CustomerResponse
from .mappers.customer_mapper import CustomerMapper
from .repository import CustomerRepository

router = APIRouter(prefix="/customers", tags=["customers"])


@router.post("")
def create_customer(customer_payload: CustomerCreate) -> CustomerResponse:
    domain = CustomerMapper.dto_to_domain(customer_payload)
    domain_answer = CustomerRepository().save_customer(domain)
    return CustomerMapper.domain_to_dto(domain_answer)

@router.get("{customer_id}")
def get_customer(customer_id: int) -> dict:
    ...