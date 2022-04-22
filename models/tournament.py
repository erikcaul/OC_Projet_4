import json
import os
from controllers.tools import Tools

class Tournament:
    """Patern for tournaments"""
    def __init__(self, name, location, date, rounds, players, players_points, time_controller, turns_number=4, description=""):
        """initialize tournament"""
        self.name = name
        self.location = location
        self.date = date
        self.rounds = rounds
        self.players = players
        self.players_points = players_points # (commence à 0) nombre de point par joueur pour le tournois (dict[instance joueur] = nombre de points)
        self.time_controller = time_controller
        self.turns_number = turns_number
        self.description = description
        self.tools = Tools()
        self.filename = "\db.json"
        db_exist = os.path.exists(self.filename)
        if db_exist != True:
            self.db = self.tools.create_db()
        else:
            self.db = self.tools.db

    def print_tournament(self): # à mettre dans report_view
        print("---------------------------------------------------")
        print("Tournament name : " + str(self.name))
        print("Tournament location : " + str(self.location))
        print("Tournament date : " + str(self.date))
        print("Tournament time controller : " + str(self.time_controller))
        print("Tournament turns number : " + str(self.turns_number))
        print("Tournament description : " + str(self.description))
        print("---------------------------------------------------")
    
    def serialize(self, all_players_list):
        rounds_list = []
        for round in self.rounds: # liste avec les élément de mes round que j'ajouterais ensuite à mon tournois = une liste de dict
            round_info = round.serialize(all_players_list)
            rounds_list.append(round_info)
        players_index_list = []
        for tournament_player in self.players:
            player_index = all_players_list.index(tournament_player)
            players_index_list.append(player_index)
        players_points_dict = self.players_points
        players_name_points_dict = {}
        for player, points in players_points_dict.items():
            player_index = all_players_list.index(player)
            players_name_points_dict[player_index] = points
        return {
            "name": self.name,
            "location": self.location,
            "date": self.date,
            "rounds": rounds_list,
            "players": players_index_list, 
            "players_points": players_name_points_dict, 
            "time_controller": self.time_controller,
            "turns_number": self.turns_number,
            "description": self.description
        }
