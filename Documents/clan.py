
from mongoengine import EmbeddedDocument, StringField

class Clan(EmbeddedDocument):
    tag = StringField(required=True)
