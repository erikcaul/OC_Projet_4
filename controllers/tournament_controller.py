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
        players_ranking = {} # (commence à 0) nombre de point par joueur pour le tournois (dict[instance joueur] = nombre de points)
        new_tournament = Tournament(
            new_tournement_info["name"],
            new_tournement_info["location"],
            new_tournement_info["date"],
            rounds,
            players,
            players_ranking,
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


    def match_making(self, tournament):
        # condition qui me dit si je suis au 1er ou  n tours
        # Si au début du premier tour, triez tous les joueurs en fonction de leur classement
        tournament_players = tournament.players

        sorted_tournament_players = sorted(tournament_players, key=lambda p: p.ranking, reverse=True)
        # To return a new list, use the sorted() built-in function...
        # newlist = sorted(ut, key=lambda x: x.count, reverse=True)
        # = sorted(ranking_dict.items(), key=operator.itemgetter(1))
        print(sorted_tournament_players)

        # Divisez les joueurs en deux moitiés, une supérieure et une inférieure.
        half = len(sorted_tournament_players)//2
        list1 = sorted_tournament_players[:half]
        list2 = sorted_tournament_players[half:]
        print(list1)
        print(list2)
        # Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur joueur de la moitié inférieure,
        # et ainsi de suite.
        # Si nous avons huit joueurs triés par rang, alors le joueur 1 est jumelé avec le joueur 5, le joueur 2 est jumelé avec le joueur 6, etc.
        
        # créer un objet game et l'ajouter à une liste
        # retourner la liste de mon instance games (avec begin_date pour chaque) 
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

        # Si nème tour autre algo pour définir les games

        
        #
        # round1 = {}
        # i = 0
        # for element1 in list1:
        #     round1[i+1] = (element1[0], list2[i][0])
        #     i+=1
        # print(round1)
        # return round1

        # Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points.

        # Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
        # Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
        # Répétez les étapes 3 et 4 jusqu'à ce que le tournoi soit terminé.


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

