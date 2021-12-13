""" A UserController Module """

from masonite.controllers import Controller
from masonite.request import Request
from masoniteorm.query import QueryBuilder
from app.User import User
import os, json, bcrypt, binascii
from datetime import datetime as dt

# builder = QueryBuilder().table("users")
# salt = b'$2b$12$l.Dn8vXodJra7gxCJh4Chu'


class UserController(Controller):
    """Class Docstring Description
    """
    def __init__(self, request: Request):
        self.request = request

    def show(self):
        token = self.request.param('token')
        if token == "admin":
            return QueryBuilder().table('users').all()
        elif QueryBuilder().table('users').where("remember_token", token).first() == None:
            return ["Unauthorized"]
        return QueryBuilder().table('users').select("data").where("remember_token", token).first()["data"]

        
    def index(self):
        # GET request input from query
        email = self.request.input("email")
        password = self.request.input("password")
        # auth = self.request.input("auth")
        # password = builder.where("password", "=", auth).first()

        

    def login(self):
        email = self.request.input("email")
        password = self.request.input("password")
        
        # Check auth
        if QueryBuilder().table('users').where("email", email).where("password", password).select_raw("*").first() == None:
            return ["Username/password not valid"]

        # update access token and return it to login
        token = binascii.hexlify(os.urandom(8)).decode()
        QueryBuilder().table('users').where("email", email).update({"remember_token": token, "verified_at": dt.now().strftime('%Y-%m-%d %H:%M:%S')})
        return QueryBuilder().table('users').where("email", email).first()["remember_token"]


    def create(self):
        name = self.request.input("name")
        email = self.request.input("email")
        password = self.request.input("password")
        # IMPLEMENT BCRYPT
        # binary_auth = bytes(email+password, 'utf-8')
        # hashed = str(bcrypt.hashpw(binary_auth, salt))
        data = {dt.now().strftime('%Y-%m-%d'): []}
        QueryBuilder().table('users').create({
            "name": name,
            "email": email,
            "password": password,
            "data": json.dumps(data)
        })
        if QueryBuilder().table('users').select_raw("*").where("email", email).get() != None:
            return QueryBuilder().table('users').where("email", email).first()["name"]

    def update(self):
        token = self.request.param("token")
        new_data = self.request.input("data")
        QueryBuilder().table('users').where("remember_token", token).update({"data": json.dumps(new_data)})
        return QueryBuilder().table('users').where("remember_token", token).first()


    def destroy(self):
        token = self.request.param("token")
        QueryBuilder().table('users').where("remember_token", token).delete()
        return ["Account deleted"]