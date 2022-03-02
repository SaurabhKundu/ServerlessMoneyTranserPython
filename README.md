# ServerlessMoneyTranserPython
A simple Python based AWS serverless application to transfer money between accounts


## You can deploy the application directly in AWS Lambda with Python runtime.
Pass the json in MoneyTransferRequest.json file as input.


The lambda function is tested locally in the `lambda_function.test.py` 
by mimicking the event and context arguments sent by AWS Lambda


## Also created a Rest web service using flask

### The endpoints are:

    HTTP GET: http://127.0.0.1:5000/customers
    HTTP GET: http://127.0.0.1:5000/accounts
    HTTP POST: http://127.0.0.1:5000/transfer
    
Same MoneyTransferRequest.json can be used as a request body for transfer endpoint