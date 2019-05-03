from mongoengine import *
from WebSearch.domain import History, User, Product

class DBManager:
    def __init__(self, db='NeuralImageSearch', host='localhost', port=27017):
        connect('mydb')

    def get_user(self):
        return User

    def get_history(self):
        return History
    
    def get_product(self):
        return Product