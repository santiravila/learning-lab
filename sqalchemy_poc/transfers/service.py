from common.enums import TransferType
from .models import Transfer
from accounts.repository import AccountRepository
from accounts.schema import AccountUpdate


class TransferService:
    def __init__(self, account_repo: AccountRepository, transfer_repo):
        self.account_repo = account_repo
        self.transfer_repo = transfer_repo

    def __deposit(self, account, amount):
        # create update method in account repo. Receive an update payload, update fields, persist delta
        new_balance = account.balance + amount
        update_payload = AccountUpdate(
            balance=new_balance
        )
        self.account_repo.update_account(account_id=account.id, account_payload=update_payload)

    def __withdraw(self, account, amount):
        # subtract from the account balance
        new_balance = account.balance - amount
        update_payload = AccountUpdate(
            balance=new_balance
        )
        self.account_repo.update_account(account_id=account.id, account_payload=account)

    def execute_transfer(self, transfer_payload) -> Transfer:
        # get account with account_id using account_repo to check it exists
        account = self.account_repo.load_account(transfer_payload.account_id)

        # call deposit or withdraw depending on transfer type with the account
        if transfer_payload.transfer_type == TransferType.DEPOSIT.value:
            self.__deposit(account=account, amount=transfer_payload.amount)
        elif transfer_payload.transfer_type == TransferType.WITHDRAWAL.value:
            self.__withdraw(account=account, amount=transfer_payload.amount)

        # map DTO to SQLAlchemy model
        transfer = Transfer(
            amount=transfer_payload.amount,
            transfer_type=transfer_payload.transfer_type,
            account_id=transfer_payload.account_id
        )

        # persist transfer for id and timestamp
        return self.transfer_repo.save(transfer)
        