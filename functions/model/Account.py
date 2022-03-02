class Account:
    account_id = ''
    account_type = ''
    balance = 0
    isActive = False

    def __init__(self, account_id, account_type, balance, active):
        self.account_id = account_id
        self.account_type = account_type
        self.balance = balance
        self.isActive = active
