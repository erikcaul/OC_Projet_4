import json
import os
from controllers.tools import Tools

class Player:
    """Patern for a player"""
    def __init__(self, family_name, first_name, birth_date, sexe, ranking):
        """initialize player"""
        self.name = family_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sexe = sexe
        self.ranking = ranking # nombre de points
        
    def print_player(self, player):
        print("---------------------------------------------------")
        print("Player family name : " + str(player.name))
        print("Player first name : " + str(player.first_name))
        print("Player birth date : " + str(player.birth_date))
        print("Player sexe : " + str(player.sexe))
        print("Player ranking : " + str(player.ranking))
        print("---------------------------------------------------")

    def dict_player(self, player):
        player_dict = {}
        player_dict["Player family name"] = player.name
        player_dict["Player first name"] = player.first_name
        player_dict["Player birth date"] = player.birth_date
        player_dict["Player sexe"] = player.sexe
        player_dict["Player ranking"] = player.ranking
        return player_dict

    def serialize_player(self, player): 
        dict_player = self.dict_player(player)
        serialize_player = json.loads(json.dumps(dict_player))
        return serialize_player
