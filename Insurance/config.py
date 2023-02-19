import os

from Insurance.logger import logging
from Insurance.exception import InsuranceException
import pymongo
from dataclasses import dataclass

@dataclass
class EnvironmentVariable:
    Mongo_Url: str = os.getenv("MONGO_DB_URL")


env_var = EnvironmentVariable()
client = pymongo.MongoClient(env_var.Mongo_Url)
print(env_var.Mongo_Url)
