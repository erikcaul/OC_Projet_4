"""Tournaments Controller"""
from views.tournament_view import TournamentView
from models.tournament import Tournament


class TournamentController:

    def __init__(self, players_all):
        self.tournament_view = TournamentView()
        self.players_all = players_all # list of all players 
        self.rounds = [] # rounds list
        # liste de tournament
        

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
        # print(new_tournament)
        return new_tournament

    def add_player(self):
        # appeler la vue "tournament" avec différentes fonctionalités, dont pour ajouter player
        self.tournament_view.prompt_add_player()

