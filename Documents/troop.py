from mongoengine import EmbeddedDocument, StringField, IntField

class Troop(EmbeddedDocument):
    name = StringField(required=True)
    level = IntField(required=True)
