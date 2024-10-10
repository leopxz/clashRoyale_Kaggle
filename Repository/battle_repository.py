# repositories/battle_repository.py

from Documents.battle import Battle

class BattleRepository:
    def count_battles_by_card_id_in_time_range(self, card_id, start_time, end_time):
        return Battle.objects(cards__list=card_id, battle_time__gte=start_time, battle_time__lte=end_time).count()

    def count_card_wins(self, card_id, start_time, end_time):
        return Battle.objects(winner__cards__list=card_id, battle_time__gte=start_time, battle_time__lte=end_time).count()

    def count_card_losses(self, card_id, start_time, end_time):
        return Battle.objects(loser__cards__list=card_id, battle_time__gte=start_time, battle_time__lte=end_time).count()

    def find_all_winning_decks_in_time_range(self, start_time, end_time):
        return Battle.objects(battle_time__gte=start_time, battle_time__lte=end_time).only('winner.deck', 'loser.deck')

    def find_all_battles_in_time_range(self, start_time, end_time):
        return Battle.objects(battle_time__gte=start_time, battle_time__lte=end_time)
    
    def find_battle_with_highest_total_card_level(self, page_request):
        # Implementar lógica para ordenar por nível total das cartas e paginar
        # Exemplo simplificado:
        return Battle.objects.order_by('-winner.totalcard.level').skip(page_request.skip).limit(page_request.limit)
