from Repository.battle_repository import BattleRepository

class BattleService:
    def __init__(self):
        self.battle_repository = BattleRepository()

    def calculate_win_loss_percentage_for_card(self, card_id, start_time, end_time):
        total_battles = self.battle_repository.count_battles_by_card_id_in_time_range(card_id, start_time, end_time)
        wins = self.battle_repository.count_card_wins(card_id, start_time, end_time)
        losses = self.battle_repository.count_card_losses(card_id, start_time, end_time)
        
        win_percentage = (wins / total_battles) * 100 if total_battles > 0 else 0.0
        loss_percentage = (losses / total_battles) * 100 if total_battles > 0 else 0.0
        return {"win_percentage": win_percentage, "loss_percentage": loss_percentage}

    def get_decks_with_more_than_x_percent_wins(self, percentage, start_time, end_time):
        all_battles = self.battle_repository.find_all_winning_decks_in_time_range(start_time, end_time)
        deck_win_counts = {}
        deck_total_counts = {}

        for battle in all_battles:
            winning_deck = battle["winner"]["deck"]
            losing_deck = battle["loser"]["deck"]

            deck_win_counts[winning_deck] = deck_win_counts.get(winning_deck, 0) + 1
            deck_total_counts[winning_deck] = deck_total_counts.get(winning_deck, 0) + 1
            deck_total_counts[losing_deck] = deck_total_counts.get(losing_deck, 0) + 1

        filtered_decks = [deck for deck, wins in deck_win_counts.items() if (wins / deck_total_counts[deck]) * 100 > percentage]
        return filtered_decks

    def calculate_losses_for_combo(self, card_ids, start_time, end_time):
        all_battles = self.battle_repository.find_all_battles_in_time_range(start_time, end_time)
        losses = sum(1 for battle in all_battles if set(card_ids).issubset(set(battle["loser"]["deck"])))
        return losses
