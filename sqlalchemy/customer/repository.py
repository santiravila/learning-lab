from pathlib import Path
import json
from .domain import Customer
from .mappers.customer_mapper import CustomerMapper
from datetime import datetime

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
                    for customer in customers_raw:
                        customer = CustomerMapper.json_to_domain(customer)
                        customers.append(customer)
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