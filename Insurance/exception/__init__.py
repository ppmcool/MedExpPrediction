import os
import sys


def error_message_detail(error: Exception, error_detail: sys) -> str:
    _, _, exc_tb = error_detail.exc_info()

    line_number = exc_tb.tb_frame.f_lineno

    # extracting file name from exception traceback
    file_name = exc_tb.tb_frame.f_code.co_filename

    # preparing error message
    error_message = f"Error occurred python script name [{file_name}]" \
                    f" line number [{exc_tb.tb_lineno}] error message [{error}]."

    return error_message


# to create own excption class need to inherit Exception class
class InsuranceException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
