import os
import logging
import jsonpickle
from functions.repo import get_account_by_id
from functions.service import validate_account_types, validate_account_owner, transfer_money, \
    validate_is_account_active

logger = logging.getLogger()


def handle_events(event):
    logger.info('handleEvents function invoked !!')

    sender_id = event.get('senderId')
    sender_account_id = event.get('senderAccountId')

    beneficiary_id = event.get('beneficiaryId')
    beneficiary_account_id = event.get('beneficiaryAccountId')
    beneficiary_account_type = event.get('beneficiaryAccountType')

    amount = event.get('amount')

    validate_account_types(beneficiary_account_type)
    validate_is_account_active(beneficiary_account_id)
    validate_account_owner(sender_id, sender_account_id, beneficiary_id, beneficiary_account_id)
    transfer_money(sender_account_id, beneficiary_account_id, amount)
    return {
            "senderBalance": get_account_by_id(sender_account_id).balance,
            "BeneficiaryBalance": get_account_by_id(beneficiary_account_id).balance
           }


def lambda_handler(event, context):
    """
        AWS serverless will invoke this handler method
    """

    logger.info(' ## Environment Variables' + " " + jsonpickle.encode(dict(**os.environ)))
    logger.info(' ## Context' + " " + jsonpickle.encode(event))
    logger.info(' ## Event' + " " + jsonpickle.encode(context))
    return handle_events(event)
