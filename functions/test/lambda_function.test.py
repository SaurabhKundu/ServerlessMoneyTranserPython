import logging
import sys
import unittest
import json
import os
from unittest import mock

import functions.lambda_function
from functions.exception.TransferFailureException import TransferFailureException
from functions.service import validate_is_account_active, is_account_owned, validate_account_types

logger = logging.getLogger()
logger.setLevel(logging.INFO)


@mock.patch.dict(os.environ)
class TestFunction(unittest.TestCase):
    """
        A function to test lambda function and invokes the same with a sample valid JSON request as event
    """

    def test_function_success(self):
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)
        event = {
            "beneficiaryId": "cus1",
            "beneficiaryAccountId": "acc1",
            "beneficiaryAccountType": "SAVINGS",
            "senderId": "cus2",
            "senderAccountType": "SAVINGS",
            "senderAccountId": "acc2",
            "amount": 100
        }
        context = {'requestId': '1234'}
        result = functions.lambda_function.lambda_handler(event, context)
        result = str(result)
        result = result.replace("\'", "\"")
        print(str(result))
        json_obj = json.loads(str(result))
        self.assertEqual(json_obj['senderBalance'], 900, "after debit values are matched")
        self.assertEqual(json_obj['BeneficiaryBalance'], 200, "after credit values are matched")
        logger.removeHandler(stream_handler)

    def test_function_when_account_is_inactive_throws_exception(self):
        self.assertRaises(TransferFailureException, validate_is_account_active, "acc3")

    def test_function_when_account_is_not_owned_throws_exception(self):
        self.assertRaises(TransferFailureException, is_account_owned, "cus1", "acc2")

    def test_function_when_account_type_is_invalid_owned_throws_exception(self):
        self.assertRaises(TransferFailureException, validate_account_types, "CURRENT")


if __name__ == '__main__':
    unittest.main()
