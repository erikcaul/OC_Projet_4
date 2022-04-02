import json
from views.player_view import PlayerView
from models.player import Player


"""Controllers for player things"""


class PlayerController:
    """Controller for player"""
    def __init__(self):
        self.players = []
        self.player_view = PlayerView()

    def create_player(self):
        new_player_info = self.player_view.prompt_player_creation()
        new_player = Player(
            new_player_info["family_name"],
            new_player_info["first_name"],
            new_player_info["birth_date"],
            new_player_info["sexe"],
            new_player_info["ranking"],
            )
        self.players.append(new_player)

    def save_player(self, player):
        serialize_player = player.serialize_player(player)
        return serialize_player
