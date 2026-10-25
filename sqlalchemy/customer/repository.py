from .domain import Customer
from .mappers.customer_mapper import CustomerMapper
from datetime import datetime
from pathlib import Path
import json

file_dir = Path.cwd() / "persistency"
file_path = file_dir / "customers.json"


class CustomerRepository:
    def __init__(self, customer_file: str | None = None) -> None:
        self.customer_file = file_path if customer_file is None else Path(customer_file)
   
    def _load(self) -> list[Customer]:
        customers = []
        file_dir.mkdir(parents=True, exist_ok=True)
        
        if self.customer_file.exists():
            try:
                with open(self.customer_file, mode="r") as f:
                    customers_raw = json.load(f)
                    customers = list(map(CustomerMapper.json_to_domain, customers_raw))
            except json.JSONDecodeError:
                return []
            return customers
        return []

    def _save(self, customers: list[Customer]):
        with open(self.customer_file, mode="w") as f:
            customers_raw = list(map(CustomerMapper.domain_to_json, customers))
            json.dump(customers_raw, f)

    def save_customer(self, customer: Customer):
        customers = self._load()
        highest_index = max(
            (c.customer_id for c in customers if c.customer_id is not None),
            default=0,
        )

        customer.customer_id = highest_index + 1
        customer.registered_at = datetime.now()
    
        customers.append(customer)

        self._save(customers)

        return customer

    def get_customer(self, customer_id: int) -> Customer:
        customers = self._load()
        
        for customer in customers:
            if customer.customer_id == customer_id:
                return customer
            
        raise ValueError(f"No saved customer with id {customer_id}")