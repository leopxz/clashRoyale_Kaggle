# models/player.py

from mongoengine import EmbeddedDocument, StringField, IntField, EmbeddedDocumentField
from .clan import Clan
from .card import Card
from .cards import Cards
from .total_card import TotalCard
from .troop import Troop
from .structure import Structure

class Player(EmbeddedDocument):  # Alterado para EmbeddedDocument
    tag = StringField(required=True, unique=True)
    clan = EmbeddedDocumentField(Clan)  # Certifique-se de que Clan é um EmbeddedDocument
    
    # Cartas no deck (card1 até card8)
    card1 = EmbeddedDocumentField(Card)  # Certifique-se de que Card é um EmbeddedDocument
    card2 = EmbeddedDocumentField(Card)
    card3 = EmbeddedDocumentField(Card)
    card4 = EmbeddedDocumentField(Card)
    card5 = EmbeddedDocumentField(Card)
    card6 = EmbeddedDocumentField(Card)
    card7 = EmbeddedDocumentField(Card)
    card8 = EmbeddedDocumentField(Card)

    # Outros campos relacionados a cartas e tropas
    cards = EmbeddedDocumentField(Cards)  # Certifique-se de que Cards é um EmbeddedDocument
    
    starting_trophies = IntField(required=True)
    crowns = IntField(required=True)
    
    totalcard = EmbeddedDocumentField(TotalCard)  # Certifique-se de que TotalCard é um EmbeddedDocument
    troop = EmbeddedDocumentField(Troop)  # Certifique-se de que Troop é um EmbeddedDocument
    structure = EmbeddedDocumentField(Structure)  # Certifique-se de que Structure é um EmbeddedDocument
