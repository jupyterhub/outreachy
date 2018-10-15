from tornado import gen, web
from jupyterhub.handlers import BaseHandler
from jupyterhub.auth import Authenticator

class MyAuthenticator(Authenticator):
    login_service = "My Service"

    @gen.coroutine
    def authenticate(self,handler,data=None):
        rawd = None

       # If we receive no data we redirect to login page
       while (rawd is None):
           try:
               rawd = handler.get_argument("data")
           except:
               handler.redirect("<The login URL>")
               return None

       # Do some verification and get the data here.
       # Get the data from the parameters send to your hub from the login page, say username, access_token and email. Wrap everythin neatly in a dictionary and return it.

       userdict = {"name": username}
       userdict["auth_state"] = auth_state = {}
       auth_state['access_token'] = verify
       auth_state['email'] = email

       #return the dictionary
       return userdict
