"""Tournaments Controller"""
from views.tournament_view import TournamentView
from models.tournament import Tournament


class TournamentController:

    def __init__(self):
        self.tournament_view = TournamentView()

    def new_tournament(self):
        new_tournement_info = self.tournament_view.prompt_tournament_creation()
        rounds = []
        players = []
        new_tournament = Tournament(new_tournement_info[0], new_tournement_info[1], new_tournement_info[2], rounds, players, new_tournement_info[4], new_tournement_info[3], new_tournement_info[5])
        print(new_tournament)
        return new_tournament

    def add_player(self):
        # appeler la vue "tournament" avec différentes fonctionalités, dont pour ajouter player
        self.tournament_view.prompt_add_player()

