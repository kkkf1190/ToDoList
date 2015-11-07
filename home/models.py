from django.db import models
from mongoengine import Document, StringField, connect,IntField

connect('employeeDB')


# Create your models here.


class ListModel(Document):
    list_id = IntField(required=True)
    list_item= StringField(required=True)
    list_type = IntField(required=True)

class ListsModel(Document):
    list_id = IntField(required=True)
    list_name = StringField(required=True)
