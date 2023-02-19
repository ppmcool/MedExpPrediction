from Insurance.logger import logging
import sys, os
from Insurance.exception import InsuranceException
from Insurance.utils import get_dataframe

"""def test_logger_exception():
    try:
        logging.info("starting")
        res=10/0
        print(res)
        logging.info("end")
    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e, sys)"""

if __name__ == "__main__":
    try:
        get_dataframe(database_name="INSURANCE", collection_name="INSURANCE_DATA")
    except Exception as e:
        print(e)
