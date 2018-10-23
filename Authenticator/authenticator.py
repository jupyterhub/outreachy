from jupyterhub.auth import Authenticator
from tornado import gen
import csv


class MyAuthenticator(Authenticator):
    @gen.coroutine
    def authenticate(self, data, handler):

        csv_dict={}
        with open('authentication.csv', mode='r') as csv_file:
            csv_data = {row["title"]: row["value"] for row in csv.DictReader(csv_file, ("title", "value"))}
            csv_dict.update(csv_data)

        if data['username'] not in csv_dict:
            self.logger.warning("No such user: %s", data['username'])
        else:

            if csv_dict[name] != data['password']:
                self.logger.warning("Incorrect password for user: %s", data['username'])
                
            else: 
                self.logger.info("user: %s has logged in ", data['username'])
                return data['username']
