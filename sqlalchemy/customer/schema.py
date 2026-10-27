from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime

# base dto shared properties
class CustomerBase(BaseModel):
    fullname: str
    email: EmailStr


class CustomerCreate(CustomerBase):
    pass


class CustomerResponse(CustomerBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    registered_at: datetime


class CustomerUpdate(CustomerBase):
    id: Optional[int] = None
    email: Optional[EmailStr] = None
    fullname: Optional[str] = None
    registered_at: Optional[datetime] = None


    
        
