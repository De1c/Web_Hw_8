from mongoengine import Document, connect
from mongoengine.fields import StringField, EmailField, BooleanField

import connect

class Contacts(Document):
    name = StringField()
    email = EmailField()
    phone = StringField()
    sending = BooleanField()
    email_priority = BooleanField()