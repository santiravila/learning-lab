from sqlalchemy.orm import Session
from .models import Account


class AccountRepository:
    def __init__(self, session: Session):
        self.session = session

    def save_account(self, account: Account) -> Account:
        self.session.save(account)
        self.session.commit()
        self.refresh(account)

        return account  