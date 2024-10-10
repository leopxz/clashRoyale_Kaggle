# models/card.py

from mongoengine import EmbeddedDocument, StringField, IntField

class Card(EmbeddedDocument):
    id = IntField(required=True)  # ID da carta
    name = StringField(required=True)
    level = IntField(required=True)
    # Adicione outros campos conforme necessário
