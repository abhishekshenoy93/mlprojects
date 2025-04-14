import sys

def error_message_detail(error, error_detail: sys):
    """
    This function returns a detailed error message including the error type, value, and traceback.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with error message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    """
    Custom exception class that inherits from the built-in Exception class. 
    It provides a detailed error message when an exception occurs.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the CustomException class with an error message and error detail.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        """
        Returns the string representation of the CustomException class.
        """
        return self.error_message

