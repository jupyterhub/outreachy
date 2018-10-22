from jupyterhub.auth import Authenticator
from tornado import gen
import csv
import logging


class MyAuthenticator(Authenticator):
    @gen.coroutine
    def authenticate(self, data, handler):

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # create a file handler
        handler = logging.FileHandler('authenticator.log')
        handler.setLevel(logging.INFO)

        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(handler)

        csv_dict={}
        with open('authentication.csv', mode='r') as csv_file:
            csv_data = {row["title"]: row["value"] for row in csv.DictReader(csv_file, ("title", "value"))}
            csv_dict.update(csv_data)

        if data['username'] not in csv_dict:
            logger.warning("No such user: %s", data['username'])
        else:

            if csv_dict[name] != data['password']:
                logger.Warnig("Incorrect password for user: %s", data['username'])
                
            else: 
                logger.info("user: %s has logged in ", data['username'])
                return data['username']
