import logging

from functions.exception.TransferFailureException import TransferFailureException
from functions.repo import get_customer_by_id, get_account_by_id

logger = logging.getLogger()


def validate_account_types(beneficiary_account_type):
    """
        cannot transfer money between current accounts, throw exception
    """
    if beneficiary_account_type == 'CURRENT':
        logger.error('cannot transfer between current accounts')
        raise TransferFailureException('cannot transfer between current accounts')


def debit_sender_balance(sender_account_id, balance):
    """
        the sender's balance will be debited
    """
    logger.info('debiting sender: {} balance'.format(sender_account_id))
    sender_account = get_account_by_id(sender_account_id)
    sender_account.balance -= balance


def credit_beneficiary_balance(beneficiary_account_id, balance):
    """
        beneficiary's balance will be credited
    """
    logger.info('crediting beneficiary: {} balance'.format(beneficiary_account_id))
    beneficiary_account = get_account_by_id(beneficiary_account_id)
    beneficiary_account.balance += balance


def transfer_money(sender_account_id, beneficiary_account_id, balance):
    debit_sender_balance(sender_account_id, balance)
    credit_beneficiary_balance(beneficiary_account_id, balance)


def validate_account_owner(sender_id, sender_account_id, beneficiary_id, beneficiary_account_id):
    """
        validates if sender and beneficiaries accounts are valid
    """
    logger.info('validating account ownership...')
    is_account_owned(sender_id, sender_account_id)
    is_account_owned(beneficiary_id, beneficiary_account_id)


def is_account_owned(owner_id, account_id):
    account_owned = False
    customer_details = get_customer_by_id(owner_id)
    for acc in customer_details.account_ids:
        if acc == account_id:
            account_owned = True

    if not account_owned:
        logger.error('account: {} is not owned by owner: {}'.format(account_id, owner_id))
        raise TransferFailureException('account: {} is not owned by owner: {}'.format(account_id, owner_id))


def validate_is_account_active(beneficiary_account_id):
    account = get_account_by_id(beneficiary_account_id)
    if not account.isActive:
        raise TransferFailureException("The account is inactive")