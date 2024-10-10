
from mongoengine import EmbeddedDocument, IntField

class TotalCard(EmbeddedDocument):
    level = IntField(required=True)
