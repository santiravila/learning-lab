from customer.schema import CustomerCreate, CustomerResponse
from customer.domain import Customer
from datetime import datetime


class CustomerMapper:
    @staticmethod
    def dto_to_domain(dto: CustomerCreate) -> Customer:
        return Customer(
            customer_id=None,
            fullname=dto.fullname,
            email=dto.email,
            registered_at=None
        )

    @staticmethod
    def domain_to_dto(domain: Customer) -> CustomerResponse:
        if domain.customer_id is None or domain.registered_at is None:
            raise ValueError("Cannot serialize unpersisted domain model.")

        return CustomerResponse(
            fullname=domain.fullname,
            email=domain.email,
            customer_id=domain.customer_id,
            registered_at=domain.registered_at
        )

    @staticmethod
    def json_to_domain(content: dict) -> Customer:
        content["registered_at"] = datetime.fromisoformat(
            content["registered_at"]
        )
        return Customer(**content)

    @staticmethod
    def domain_to_json(customer: Customer) -> dict:
        if customer.registered_at is None:
            raise ValueError("Cannot persist a customer without registration date.")
        return {
            "customer_id": customer.customer_id,
            "fullname": customer.fullname,
            "email": customer.email,
            "registered_at": customer.registered_at.isoformat()
        }