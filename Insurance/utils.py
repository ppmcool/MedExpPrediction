from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os, sys
import pandas as pd
from Insurance.config import client


def get_dataframe(database_name: str, collection_name: str) -> pd.DataFrame:
    try:
        logging.info("Reading From DataBase")
        df = pd.DataFrame(list(client[database_name][collection_name].find()))

        if "_id" and 'Unnamed: 0' in df.columns:
            logging.info("Dropping columns")
            df = df.drop(['_id', 'Unnamed: 0'], axis=1)
        logging.info(f"found columns:{df.columns}")
        logging.info(f'size of data :{df.shape}')

        return df

    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(str(e), sys)
