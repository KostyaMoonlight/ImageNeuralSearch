from mongoengine import *

class Product(Document):
    id = StringField()
    name = StringField()
    url = StringField()
    image = ImageField()
    encoding = ListField(FloatField())
