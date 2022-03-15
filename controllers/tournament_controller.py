"""Tournaments Controller"""
from models.player import Player
from models.round import Round
from models.game import Game
from views.tournament_view import TournamentView
from models.tournament import Tournament
from controllers.tools import Tools
import datetime


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
        players_points = {} # (commence à 0) nombre de points par joueur pour le tournois (dict[instance joueur] = nombre de points)
        new_tournament = Tournament(
            new_tournement_info["name"],
            new_tournement_info["location"],
            new_tournement_info["date"],
            rounds,
            players,
            players_points,
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
            print('Tournament is beginning...')
            return
        pick_player = self.tournament_view.pick_up_player(self.players_all, pick_tournament.players)
        pick_tournament.players.append(pick_player)
        pick_tournament.players_points[pick_player] = 0

    def already_players_list(self, player):
        """List of the players whose have already played with the player"""
        already_players_played_list = []
        for round in self.rounds:
            for game in round.games:
                if game.player_1 == player:
                    already_players_played_list.append(game.player_2)
                    break
                if game.player_2 == player:
                    already_players_played_list.append(game.player_1)
                    break
        return already_players_played_list

    def match_making(self, tournament):
        # Validate if it is the first round or not
        tournament_turn_number = len(tournament.rounds)
        if tournament_turn_number == 0:
            # First round : Sorting all the players with their ranking
            tournament_players = tournament.players
            sorted_tournament_players = sorted(tournament_players, key=lambda p: p.ranking, reverse=True)
            half = len(sorted_tournament_players)//2
            list1 = sorted_tournament_players[:half]
            list2 = sorted_tournament_players[half:]
            # Create a Game object and add it to a list
            games_list = []
            i = 0
            for i in (half - 1):
                new_game = Game(
                    list1[i],
                    list2[i],
                    datetime.datetime.now()
                )
                games_list.append(new_game)
            return games_list
        else:
            # N round : Sorting all the players with their points number
            players_points_dict = tournament.players_points
            sorted_players_points_dict = sorted(players_points_dict.items(), key=lambda item: (item[1], item[0].ranking))
            sorted_players_list = map(lambda item: item[0], sorted_players_points_dict)
            # Create a Game object and add it to a list
            games_list = []
            
            while len(sorted_players_list) > 0:
                play1 = sorted_players_list[0]
                already_players_played_list = self.already_players_played_list(play1)
                list_rest_players = sorted_players_list - already_players_played_list - [play1]
                new_game = Game(
                    play1,
                    list_rest_players[0],
                    datetime.datetime.now()
                )
                games_list.append(new_game)
                sorted_players_list.remove(play1)
                sorted_players_list.remove(list_rest_players[0])
            return games_list
            

    def create_a_round(self):
        pick_tournament = self.tournament_view.pick_up_tournament(self.tournaments_list)
        tournament_players_count = len(pick_tournament.players)
        tournament_rounds_count = pick_tournament.turns_number
        # vérifer que le nombre de joueur est pair
        if tournament_players_count % 2 == 0:
            # + vérifier qu'il y a suffisemment de joureurs pour faire tous les tours du tournois
            if tournament_players_count // 2 == tournament_rounds_count:
                games = self.match_making(pick_tournament)
                begin_date = datetime.datetime.now()
                tournament_turn_number = len(pick_tournament.rounds) + 1
                round_name = 'Round' + str(tournament_turn_number)
                new_round = Round(
                    round_name,
                    games,
                    begin_date
                )
                print(new_round.round_name)
                print(new_round.games)
        else:
            print("Add more player please !")
            return

    def play_a_round(self):
        pick_tournament = self.tournament_view.pick_up_tournament(self.tournaments_list)
        # Validate Round exists

        # Select last Round

        # Prompt view for scores completion
        # boucle sur les games
        for game in round.games:
            game_result = self.tournament_view.prompt_game_result(game)
            game.player_1_win

        # update players classement in the tournament
        # update player_ranking of the Tournament
