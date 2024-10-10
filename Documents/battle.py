# models/battle.py

from mongoengine import Document, StringField, EmbeddedDocumentField, DateTimeField
from .player import Player

class Battle(Document):
    meta = {'collection': 'battle'}
    id = StringField(primary_key=True)
    battle_time = DateTimeField(required=True)
    winner = EmbeddedDocumentField(Player, required=True)
    loser = EmbeddedDocumentField(Player, required=True)
