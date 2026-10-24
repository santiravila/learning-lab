from pydantic import BaseModel, EmailStr
from datetime import datetime

# base dto shared properties
class CustomerBase(BaseModel):
    fullname: str
    email: EmailStr


class CustomerCreate(CustomerBase):
    pass


class CustomerResponse(CustomerBase):
    customer_id: int
    registered_at: datetime
