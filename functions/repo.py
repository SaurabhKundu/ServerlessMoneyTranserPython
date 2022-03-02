from functions.model.Account import Account
from functions.model.Customer import Customer

"""
    A mock repository to populate dummy data 
"""


accounts = [
    Account('acc1', 'SAVINGS', 100, True),
    Account('acc2', 'CURRENT', 1000, True),
    Account('acc3', 'SAVINGS', 200, False),
    Account('acc4', 'SAVINGS', 10000, True)
]

customer1 = Customer('cus1', 'cus-name-1', 'cus1@yz.com', ['acc1'])
customer2 = Customer('cus2', 'cus-name-2', 'cus2@yz.com', ['acc2'])
customer3 = Customer('cus3', 'cus-name-3', 'cus3@yz.com', ['acc3'])
customer4 = Customer('cus4', 'cus-name-4', 'cus4@yz.com', ['acc4'])

customer_list = [customer1, customer2, customer3, customer4]


def get_customers():
    return customer_list


def get_customer_by_id(customer_id):
    for cus in customer_list:
        if cus.customer_id == customer_id:
            return cus


def get_accounts():
    return accounts


def get_account_by_id(account_id):
    for acc in accounts:
        if acc.account_id == account_id:
            return acc

