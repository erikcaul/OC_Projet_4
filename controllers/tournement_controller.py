"""Tournaments Controller"""


class TournamentController:

    def __init__(self, view_tournament_creation):
        self.view_tournament_creation = view_tournament_creation

    def new_tournament(self):
        self.view_tournament_creation.prompt_tournament_info()

    def add_player(self):
        # appeler la vue "tournament" avec différentes fonctionalités, dont pour ajouter player
        pass


