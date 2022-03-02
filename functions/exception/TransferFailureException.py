class TransferFailureException(Exception):
    """Exception raised for errors in the input salary.
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
