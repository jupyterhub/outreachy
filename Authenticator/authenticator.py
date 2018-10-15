from jupyterhub.auth import Authenticator
from tornado import gen
import csv


class MyAuthenticator(Authenticator):

    @gen.coroutine
    def authenticate(self,handler,data):
        csv_uu={}
        with open('authentication.csv', mode='r') as csv_file:
            csv_data = {row["title"]: row["value"] for row in csv.DictReader(csv_file, ("title", "value"))}
            csv_uu.update(csv_data)

        password = input("password")
        username=input("username")

        if csv_uu[username] == data['password']:
            return data['username']
            