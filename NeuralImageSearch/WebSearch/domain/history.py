from mongoengine import *

class History(Document):
    user_login = StringField()
    product_id = StringField()
    distance = FloatField()
    user_image = ImageField()
    product_image = ImageField()
    user_image_encoding = ListField(FloatField())
