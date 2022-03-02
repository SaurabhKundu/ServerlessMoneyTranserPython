import logging
import jsonpickle
import flask
from flask import Response
from flask import request
from functions.repo import get_account_by_id, get_accounts, get_customers
from functions.service import transfer_money, validate_account_owner, validate_account_types, validate_is_account_active

logger = logging.getLogger()

app = flask.Flask(__name__)
MIME_TYPE = 'application/json'
SUCCESS_CODE = 200


@app.route('/accounts', methods=['GET'])
def get_accounts_details():
    """
        A rest API endpoint to get all the accounts
    """
    return Response(jsonpickle.encode(get_accounts()), status=SUCCESS_CODE, mimetype=MIME_TYPE)


@app.route('/customers', methods=['GET'])
def get_customers_details():
    """
        A rest API endpoint to get all the customers
    """
    return Response(jsonpickle.encode(get_customers()), status=SUCCESS_CODE, mimetype=MIME_TYPE)


@app.route('/transfer', methods=['POST'])
def transfer_balance():
    """
        A rest API endpoint to transfer accounts between accounts
    """
    req = request.get_json()
    beneficiary_account_type = req["beneficiaryAccountType"]
    sender_id = req["senderId"]
    sender_account_id = req["senderAccountId"]
    beneficiary_id = req["beneficiaryId"]
    beneficiary_account_id = req["beneficiaryAccountId"]
    amount = req["amount"]

    validate_account_types(beneficiary_account_type)
    validate_is_account_active(beneficiary_account_id)
    validate_account_owner(sender_id, sender_account_id, beneficiary_id, beneficiary_account_id)
    transfer_money(sender_account_id, beneficiary_account_id, amount)
    return Response(
        jsonpickle.encode(
            {
                "senderBalance": get_account_by_id(sender_account_id).balance,
                "BeneficiaryBalance": get_account_by_id(beneficiary_account_id).balance
            }
        ),
        status=SUCCESS_CODE,
        mimetype=MIME_TYPE)


if __name__ == '__main__':
    app.run()
