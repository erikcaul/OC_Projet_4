import os
from controllers.tools import Tools


class Tournament:
    """Patern for tournaments"""
    def __init__(self,
                 name,
                 location,
                 date,
                 rounds,
                 players,
                 players_points,
                 time_controller,
                 turns_number=4,
                 description=""
                 ):
        """initialize tournament"""
        self.name = name
        self.location = location
        self.date = date
        self.rounds = rounds
        self.players = players
        self.players_points = players_points
        self.time_controller = time_controller
        self.turns_number = turns_number
        self.description = description
        self.tools = Tools()
        self.filename = r'\db.json'
        db_exist = os.path.exists(self.filename)
        if db_exist is not True:
            self.db = self.tools.create_db()
        else:
            self.db = self.tools.db

    def serialize(self, all_players_list):
        rounds_list = []
        for round in self.rounds:
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
