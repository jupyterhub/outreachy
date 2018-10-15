from jupyterhub.auth import Authenticator
from tornado import gen
import csv


class MyAuthenticator(Authenticator):

    @gen.coroutine
    def authenticate(self,handler,data):
        csv_dict={}
        with open('authentication.csv', mode='r') as csv_file:
            csv_data = {row["title"]: row["value"] for row in csv.DictReader(csv_file, ("title", "value"))}
            csv_dict.update(csv_data)

        if csv_dict[username] == data['password']:
            return data['username']
        else: 
            return None

            