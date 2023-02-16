import json

import pymongo
import pandas as pd
import certifi

#ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://Pritam:As2Tew4f2b1nlbRV@cluster0.dvagmwz.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = "Insurance.csv"
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = 'INSURANCE_DATA'

if __name__=='__main__':
    df=pd.read_csv('Insurance.csv')
    print("shape of data",df.shape)

    df.reset_index(drop=True ,inplace=True) # to reset index

    json_record=list(json.loads(df.T.to_json()).values())  # as mongo db stores key value pair we need to transpose and conveert to json

    print(json_record[0])
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)