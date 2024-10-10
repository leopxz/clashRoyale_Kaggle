from Repository.troop_repository import TroopRepository

class TroopService:
    def __init__(self):
        self.troop_repository = TroopRepository()

    def get_card_names_by_ids(self, card_ids):
        return self.troop_repository.find_card_names_by_ids(card_ids)
