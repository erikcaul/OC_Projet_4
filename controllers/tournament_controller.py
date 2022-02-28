"""Tournaments Controller"""
from models.player import Player
from models.round import Round
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
        # Au début du premier tour, triez tous les joueurs en fonction de leur classement.
        # trier tous les joueurs en fonction de leur classement
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
        # retourner la liste de mes instances game (avec begin_date pour chaque)

        round1 = {}
        i = 0
        for element1 in list1:
            round1[i+1] = (element1[0], list2[i][0])
            i+=1
        print(round1)
        return round1
        # Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points.

        # Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
        # Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
        # Répétez les étapes 3 et 4 jusqu'à ce que le tournoi soit terminé.

    
    def create_a_round(self):
        pick_tournament = self.tournament_view.pick_up_tournament(self.tournaments_list)
        tournament_players_count = len(pick_tournament.players)
        if tournament_players_count < 2 : 
            # vérifer que le nombre de joueur est pair 
            # + vérifier qu'il y a suffisemment de joureurs pour faire tous les tours du tournois
            print("Add more player please !")
            return

        games = self.match_making(pick_tournament)
        begin_date = datetime.datetime.now()
        end_date = datetime.datetime # quand on va fermer le tour
        # curr_date = datetime.datetime
        # begin_date = datetime.datetime.strptime(curr_date, "%m/%d/%y")
        # end_date = begin_date + datetime.timedelta(days=1)
        # end_date = datetime.datetime.strptime(curr_date, "%m/%d/%y")
        new_round = Round(
            'round1',
            games,
            begin_date,
            end_date
        )
        print(new_round.round_name)
        print(new_round.games)
        print(new_round.begin_date)
        print(new_round.end_date)
