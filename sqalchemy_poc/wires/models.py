from infrastructure.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Wire(Base):
    __tablename__ = "wires"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] #redundant? think about it
    # this class decides the amount of each transaction, its type and both 
    # have the same timestamp?