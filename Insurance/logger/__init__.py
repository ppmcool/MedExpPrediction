import logging
from datetime import datetime
import os

LOG_DIR = "Insurance_Log"

LOG_TIMESTAMP = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'

LOG_FILENAME = "log-{LOG_TIME}.log"

LOG_PATH = os.path.join(LOG_DIR, LOG_FILENAME)

os.makedirs(LOG_DIR,  exist_ok=True)

logging.basicConfig(filename=LOG_PATH,
filemode='w',
format='%(asctime)s %(clientip)-15s %(user)-8s %(message)s',
level=logging.INFO)
