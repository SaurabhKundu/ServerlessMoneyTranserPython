class Customer:
    customer_id = ''
    customer_name = ''
    email_id = ''
    account_ids = []

    def __init__(self, customer_id, customer_name, email_id, account_ids):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email_id = email_id
        self.account_ids = account_ids
