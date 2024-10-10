
from mongoengine import EmbeddedDocument, ListField, IntField

class Cards(EmbeddedDocument):
    list = ListField(IntField(), required=True)  # Lista de IDs de cartas

