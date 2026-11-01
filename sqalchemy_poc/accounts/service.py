from .schema import AccountCreate, AccountResponse
from .models import Account
from customers.repository import CustomerRepository
from .repository import AccountRepository


class AccountService:
    def __init__(
        self,
        customer_repo: CustomerRepository,
        account_repo: AccountRepository    
    ):
        self.customer_repo = customer_repo
        self.account.repo = account_repo

    def add_account(self, account_payload: AccountCreate) -> Account:
        # check a customer with customer_id exists. get_customer validates automatically
        customer = self.customer_repo.get_customer(account_payload.customer_id)
        
        new_account = Account(
            account_type=account_payload.account_type,
            balance=account_payload.balance,
            password=account_payload.password,

            # backpopulates makes it so customer knows new account has been appended to its list
            customer=customer
        )

        return self.account_repo.save(new_account)


        
        