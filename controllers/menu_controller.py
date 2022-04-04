"""main loop controller : user chooses between options"""

from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_management import ReportManagement
from controllers.tools import Tools
# from tinydb import TinyDB, Query
import os


"""Un contrôleur qui va faire main loop (choix option),
avant le choix, va appeler la vue "menu" pour afficher les options et ensuite attendre input
Use an infinite loop to show the menu options.
Ask the user for the options
Use if-elif-else to determine what to do according to the user input. """


class MainLoop:
    def __init__(self, menu_view, active=True):
        self.menu_view = MenuView()
        self.tools = Tools()
        self.active = active
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController(self.player_controller.players)
        self.report_management = ReportManagement(self.player_controller, self.tournament_controller)
        self.filename = "\db.json"
        db_exist = os.path.exists(self.filename)
        if db_exist != True:
            self.db = self.tools.create_db()
        else:
            self.db = self.filename

    def run(self):
        """Run the menu option"""
        # utiliser un dict avec en key le numero option à choisir str, et en valeur mettre la ref. fonction

        menu = {
            "1": self.tournament_controller.new_tournament,
            "2": self.player_controller.create_player,
            "3": self.tournament_controller.add_player,
            "4": self.tournament_controller.create_a_round,
            "5": self.tournament_controller.play_a_round,
            "6": self.tournament_controller.update_player_ranking,
            "7": self.report_management.choose_a_report,
            "8": self.save_function,
            # "9": self.load_function
            "9": self.stop_game
        }

        while self.active:
            choice = self.menu_view.prompt_menu_choice()
            if choice in menu:
                menu[choice]()
            else:
                print("invalid option")

        print("Thanks and have a good day!")

    def save_function(self):
        # save function for players
        players_table = self.db.table('Players')
        players = self.player_controller.players
        for player in players:
            serialize_player = self.player_controller.save_player(player)
            players_table.insert(serialize_player)
        # save function for tournaments
        tournament_table = self.db.table('Tournaments')
        tournaments_list = self.tournament_controller.tournaments_list
        for tournament in tournaments_list:
            serialize_tournament = self.tournament_controller.save_tournament(tournament)
            tournament_table.insert(serialize_tournament)

    def load_function(self):
        pass

    def stop_game(self):
        self.active = False
