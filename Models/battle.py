from mongoengine import Document, EmbeddedDocumentField, DateTimeField
from .player import Player
from Documents.cards import Cards

class Battle(Document):
    meta = {'collection': 'battle'}
    
    winner = EmbeddedDocumentField(Player, required=True)
    loser = EmbeddedDocumentField(Player, required=True)
    battle_time = DateTimeField(required=True)
    cards = EmbeddedDocumentField(Cards, required=True)