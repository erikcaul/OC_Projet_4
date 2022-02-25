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
        if pick_tournament is None: 
            return
        if len(pick_tournament.rounds) != 0:
            return 
        pick_player = self.tournament_view.pick_up_player(self.players_all, pick_tournament.players)
        pick_tournament.players.append(pick_player) 

    def create_a_round(self):
        pick_tournament = self.tournament_view.pick_up_tournament(self.tournaments_list)
        tournament_players_count = len(pick_tournament.players)
        if tournament_players_count < 2 :
            print("Add more player please ! ")
            return
        self.tools.match_making(pick_tournament)
        print(pick_tournament.name)
        print(pick_tournament.players)
        print(tournament_players_count)