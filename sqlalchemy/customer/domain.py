import datetime
from dataclasses import dataclass


@dataclass
class Customer:
    customer_id: int | None
    fullname: str 
    email: str
    registered_at: datetime.datetime | None


