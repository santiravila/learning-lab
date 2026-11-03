from sqlalchemy.orm import Session
from .models import Account


class AccountRepository:
    def __init__(self, session: Session):
        self.session = session

    def save_account(self, account: Account) -> Account:
        
        self.session.add(account)
        self.session.commit()
        self.session.refresh(account)

        return account  

    def load_account(self, account_id: int):
        account = self.session.get(Account, account_id)

        if not account:
            raise ValueError("No account persisted with id {account_id}")

        return account