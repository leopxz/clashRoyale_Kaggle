from mongoengine import EmbeddedDocument, IntField

class Structure(EmbeddedDocument):
    count = IntField(required=True)