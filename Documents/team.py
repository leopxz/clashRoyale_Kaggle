

from mongoengine import EmbeddedDocument, EmbeddedDocumentField
from .card import Card

class Team(EmbeddedDocument):
    card1 = EmbeddedDocumentField(Card, required=True)
