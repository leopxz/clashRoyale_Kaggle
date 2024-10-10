# repositories/troop_repository.py

from Documents.troop import Troop

class TroopRepository:
    def find_card_names_by_ids(self, card_ids):
        troops = Troop.objects(team__card1__id__in=card_ids)
        return [troop.team.card1.name for troop in troops]
