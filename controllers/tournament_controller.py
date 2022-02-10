"""Tournaments Controller"""
from models.player import Player
from views.tournament_view import TournamentView
from models.tournament import Tournament
from controllers.tools import Tools


class TournamentController:

    def __init__(self, players_all):
        self.tournament_view = TournamentView()
        self.tools = Tools()
        self.players_all = players_all # list of all players 
        self.rounds = [] # rounds list
        self.tournaments_list = [] # liste de tournament
        

    def new_tournament(self):
        new_tournement_info = self.tournament_view.prompt_tournament_creation()
        rounds = []
        players = [] # liste des players du tournament
        new_tournament = Tournament(
            new_tournement_info["name"], 
            new_tournement_info["location"], 
            new_tournement_info["date"], 
            rounds, 
            players, 
            new_tournement_info["time_controller"],
            new_tournement_info["turns_number"], 
            new_tournement_info["description"]
            )       
        self.tournaments_list.append(new_tournament)

    def add_player(self):
        pick_tournament = self.tournament_view.pick_up_tournament(self.tournaments_list)
        players_list_for_choiced_tournament = pick_tournament.players
        for player in self.players_all:
            while player not in players_list_for_choiced_tournament:     
                players_list_for_choiced_tournament.append(self.tournament_view.pick_up_player(self.players_all))
