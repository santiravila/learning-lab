from infrastructure.database import Base
from sqlalchemy import ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import Enum
from datetime import datetime


class TransferType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


class Transfer(Base):
    __tablename__ = "bank_transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(nullable=False)
    transfer_type: Mapped[TransferType] = mapped_column(
        SQLEnum(TransferType, "transfer_type")
    )
    timestamp: Mapped[datetime]

    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), nullable=False)
    account: Mapped["Account"] = relationship(backpropagates="accounts")

    wire_id: Mapped[int] = mapped_column(ForeignKey("wires.id"))
    wire: Mapped["Wire"] = relationship(backpropagates="wires")