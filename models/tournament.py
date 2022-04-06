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

    def print_tournament(self, tournament):
        print("---------------------------------------------------")
        print("Tournament name : " + str(tournament.name))
        print("Tournament location : " + str(tournament.location))
        print("Tournament date : " + str(tournament.date))
        print("Tournament time controller : " + str(tournament.time_controller))
        print("Tournament turns number : " + str(tournament.turns_number))
        print("Tournament description : " + str(tournament.description))
        print("---------------------------------------------------")
    
    def dict_tournament(self, tournament): # print_tournamnet et serialize_tournament séparés
        tournament_dict = {}
        tournament_dict["Tournament name"] = tournament.name
        tournament_dict["Tournament location"] = tournament.location
        tournament_dict["Tournament date"] = str(tournament.date) # vérifier sur web si il n'y a pas mieux
        tournament_dict["Tournament rounds"] = []
        if len(tournament.rounds) != 0:
            for round in tournament.rounds:
                round_dict = round.dict_round(round)
                tournament_dict["Tournament rounds"].append(round_dict)
        tournament_dict["Tournament players"] = []
        if len(tournament.players) != 0:
            for player in tournament.players: # ajouter l'index du joueur dans la liste globale - avoir une liste d'index à la place d'une liste de joueur
                player_dict = player.dict_player(player) # différencier affichage et serialization 
                tournament_dict["Tournament players"].append(player_dict)
        players_points_dict = tournament.players_points
        players_name_points_dict = {}
        for key, value in players_points_dict.items():
            players_name_points_dict[key.name] = value
        tournament_dict["Tournament players points"] = players_name_points_dict
        tournament_dict["Tournament time controller"] = tournament.time_controller
        tournament_dict["Tournament turns number"] = tournament.turns_number
        tournament_dict["Tournament description"] = tournament.description
        return tournament_dict

    def serialize_tournament(self, tournament): # transformation our base de donnée
        dict_tournament = self.dict_tournament(tournament)
        serialize_tournament = json.loads(json.dumps(dict_tournament)) # pas serializer
        return serialize_tournament
