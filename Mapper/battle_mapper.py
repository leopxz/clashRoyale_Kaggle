# battle_mapper.py
from Models.battle import Battle
from Models.player import Player
from DTOs.battle_dto import BattleDTO
from DTOs.player_dto import PlayerDTO

class BattleMapper:

    @staticmethod
    def to_dto(battle: Battle) -> BattleDTO:
        """Converte um objeto Battle em um objeto BattleDTO."""
        battle_dto = BattleDTO()
        battle_dto.battle_time = battle.battle_time

        # Mapear o Winner
        winner_dto = BattleMapper.to_player_dto(battle.winner)
        battle_dto.winner = winner_dto

        # Mapear o Loser
        loser_dto = BattleMapper.to_player_dto(battle.loser)
        battle_dto.loser = loser_dto

        return battle_dto

    @staticmethod
    def to_player_dto(player: Player) -> PlayerDTO:
        """Converte um objeto Player em um objeto PlayerDTO."""
        if not player:
            return None  # Retorna None se o jogador não existir
        
        player_dto = PlayerDTO()
        player_dto.tag = player.tag
        player_dto.clan_tag = player.clan.tag if player.clan else None  # Verifica se o clan não é None
        player_dto.cards = player.cards  # Certifique-se de que o método retorna uma lista de IDs de cartas

        return player_dto
