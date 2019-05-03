from mongoengine import *

class User(Document):
    login = StringField()
    name = StringField()
    surname = StringField()
    age = IntField()
    email = EmailField()
    password = StringField()
