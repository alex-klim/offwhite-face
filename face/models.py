import datetime
from django.db import models
from mongoengine import fields, Document, connect

from core.settings import DBNAME

#connect(DBNAME)

class Product(Document):
    site_product_id = fields.StringField()
    name = fields.StringField()
    categories = fields.StringField()
    description = fields.StringField()
    material = fields.StringField()
    url = fields.StringField()
    images = fields.ListField()
    site = fields.StringField()


class Price(Document):
    site_product_id = fields.StringField()
    price = fields.StringField()
    size = fields.ListField()
    color = fields.StringField()
    stock_level = fields.StringField()
    currency = fields.StringField()
    date = fields.DateTimeField(default=datetime.datetime.now)
