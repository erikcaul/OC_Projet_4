"""Tournaments Controller"""
import time
from models.round import Round
from models.game import Game
from views.tournament_view import TournamentView
from models.tournament import Tournament
from controllers.tools import Tools


class TournamentController:

    def __init__(self, players_all):
        self.tournament_view = TournamentView()
        self.tools = Tools()
        self.players_all = players_all  # list of all players
        self.rounds = []  # rounds list
        self.tournaments_list = []  # tournaments list

    def new_tournament(self):
        new_tournement_info = self.tournament_view.prompt_tournament_creation()
        rounds = []
        players = []  # players list for the tournament
        players_points = {}  # (begin at 0) dict[player] = player_points
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
        pick_tournament = self.tournament_view.pick_up_tournament(
                                               self.tournaments_list
                                               )
        if pick_tournament is None:
            return
        if len(pick_tournament.rounds) != 0:
            print('Tournament is beginning...')
            return
        if len(pick_tournament.players) < (int(pick_tournament.turns_number)
                                           * 2):
            pick_player = self.tournament_view.pick_up_player(
                                               self.players_all,
                                               pick_tournament.players
                                               )
            pick_tournament.players.append(pick_player)
            pick_tournament.players_points[pick_player] = 0
        else:
            print("There are enough players in this tournament")

    def already_players_list(self, player):
        """List of the players whose have already played with the player"""
        already_players_played_list = []
        if self.rounds is None:
            return
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
            sorted_tournament_players = sorted(
                                              tournament_players,
                                              key=lambda p: p.ranking,
                                              reverse=True
                                              )
            half = len(sorted_tournament_players)//2
            list1 = sorted_tournament_players[:half]
            list2 = sorted_tournament_players[half:]
            # Create a Game object and add it to a list
            games_list = []
            # i = 0
            for i in range(half):
                new_game = Game(
                    list1[i],
                    list2[i],
                    time.asctime()
                )
                games_list.append(new_game)
            return games_list
        else:
            # N round : Sorting all the players with their points number
            players_points_dict = tournament.players_points
            sorted_players_points_dict = sorted(
                                                players_points_dict.items(),
                                                key=lambda item:
                                                (item[1], item[0].ranking)
                                                )
            sorted_players_list = map(lambda item: item[0],
                                      sorted_players_points_dict
                                      )
            sorted_players_list = list(sorted_players_list)
            # Create a Game object and add it to a list
            games_list = []
            if len(sorted_players_list) != 0:
                while len(sorted_players_list) > 0:
                    play1 = sorted_players_list[0]
                    already_players_played_list = self.already_players_list(
                                                       play1
                                                       )
                    list_rest_players = (set(sorted_players_list)
                                         - set(already_players_played_list)
                                         - set([play1])
                                         )
                    list_rest_players = list(list_rest_players)
                    if len(list_rest_players) != 0:
                        new_game = Game(
                            play1,
                            list_rest_players[0],
                            time.asctime()
                        )
                        games_list.append(new_game)
                        sorted_players_list.remove(play1)
                        sorted_players_list.remove(list_rest_players[0])
                    else:
                        print("No player left")
            else:
                return
            return games_list

    def create_a_round(self):
        pick_tournament = self.tournament_view.pick_up_tournament(
                                               self.tournaments_list
                                               )
        if pick_tournament is None:
            return
        tournament_players_count = len(pick_tournament.players)
        tournament_rounds_count = int(pick_tournament.turns_number)
        if tournament_players_count % 2 == 0:
            if tournament_players_count // 2 == tournament_rounds_count:
                games = self.match_making(pick_tournament)
                begin_date = time.asctime()
                tournament_turn_number = len(pick_tournament.rounds) + 1
                round_name = 'Round' + str(tournament_turn_number)
                new_round = Round(
                    round_name,
                    games,
                    begin_date
                )
                pick_tournament.rounds.append(new_round)
                print("Round created with success")
        else:
            print("Add more player please !")
            return

    def play_a_round(self):
        pick_tournament = self.tournament_view.pick_up_tournament(
                                               self.tournaments_list
                                               )
        if pick_tournament is None:
            return
        # Validate Round exists
        if len(pick_tournament.rounds) > 0:
            # Select last Round
            current_round = pick_tournament.rounds[-1]
            for game in current_round.games:
                # pick_up_player for the winner
                game_result = self.tournament_view.prompt_games_results(game)
                if game_result == '1':
                    game.player_1_win = True
                    game.player_2_win = False
                    game.end_date = time.asctime()
                    pick_tournament.players_points[game.player_1] += 1
                elif game_result == '2':
                    game.player_1_win = False
                    game.player_2_win = True
                    game.end_date = time.asctime()
                    pick_tournament.players_points[game.player_2] += 1
                elif game_result == '0':
                    game.player_1_win = False
                    game.player_2_win = False
                    game.end_date = time.asctime()
                    pick_tournament.players_points[game.player_1] += 0.5
                    pick_tournament.players_points[game.player_2] += 0.5
                else:
                    print("Incorrect answer")
            current_round.end_date = time.asctime()
            print("Tournament players points : ")
            players_points_dict = pick_tournament.players_points
            players_name_points_dict = {}
            for key, value in players_points_dict.items():
                players_name_points_dict[key.name] = value
        else:
            print("No round in the tournament existed")

    def update_player_ranking(self):
        # pick_up_player
        pick_up_player = self.tournament_view.pick_up_player(
                                              self.players_all,
                                              []
                                              )
        if pick_up_player is None:
            return
        print("Player selected : " + pick_up_player.name)
        # prompt new score
        new_score = input('Please enter the new score (selected player) :\n')
        pick_up_player.ranking = new_score
        print(pick_up_player.name + " = " + pick_up_player.ranking)

    def serialize_players_list(self, tournament):
        serialize_players_list = []
        for player_globale_list in self.players_all:
            for player_tournament_list in tournament.players:
                if player_tournament_list == player_globale_list:
                    index_list = self.players_all.index(player_globale_list)
                    serialize_players_list.append(index_list)
        return serialize_players_list

    def load_tournament_from_bd(self, load_tournament_info):
        tournament_players_list = []
        for index in load_tournament_info["players"]:
            tournament_players_list.append(self.players_all[index])
        rounds_list = []
        for round in load_tournament_info["rounds"]:
            load_round = self.round_into_object(round)
            rounds_list.append(load_round)
        tournament_players_points = {}
        for index, points in load_tournament_info["players_points"].items():
            tournament_players_points[self.players_all[int(index)]] = points
        new_tournament = Tournament(
            load_tournament_info["name"],
            load_tournament_info["location"],
            load_tournament_info["date"],
            rounds_list,
            tournament_players_list,
            load_tournament_info["players_points"],
            load_tournament_info["time_controller"],
            load_tournament_info["turns_number"],
            load_tournament_info["description"]
            )
        self.tournaments_list.append(new_tournament)

    def round_into_object(self, round):
        games_list = []
        load_round = Round(
            round["round_name"],
            round["games"],
            round["begin_date"],
            round["end_date"]
        )
        for game in load_round.games:
            game = Game(
                self.players_all[game["player_1"]],
                self.players_all[game["player_2"]],
                game["begin_date"],
                game["player_1_win"],
                game["player_2_win"],
                game["end_date"]
            )
        games_list.append(game)
        load_round.games = games_list
        return load_round
