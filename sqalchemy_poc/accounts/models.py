from infrastructure.database import Base
from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import Enum

class AccountType(Enum):
    CURRENT="current"
    SAVINGS="savings"


class Account(Base):
    __tablename__ = "accounts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    account_type: Mapped[AccountType] = mapped_column(
        SQLEnum(AccountType, name="account_types")
    )
    balance: Mapped[float] = mapped_column()
    password: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))

    customer: Mapped["Customer"] = relationship(back_populates="accounts")

    def __repr__(self):
        return f"id:{self.id}, accounttype:{self.account_type}, balance: {self.balance}, password: {self.password}, created_at: {self.created_at}, customer_id:{self.customer_id}"