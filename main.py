from Insurance.logger import logging
import sys,os
from Insurance.exception import InsuranceException


def test_logger_exception():
    try:
        logging.info("starting")
        res=10/0
        print(res)
        logging.info("end")
    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e, sys)


if __name__ == "__main__":
    try:
        test_logger_exception()
    except Exception as e:
        print(e)
