"""main loop controller : user chooses between options"""

from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_management import ReportManagement
from controllers.tools import Tools
import os


class MainLoop:
    """Use an infinite loop to show the menu options"""
    def __init__(self, menu_view, active=True):
        self.menu_view = MenuView()
        self.tools = Tools()
        self.active = active
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController(
                                        self.player_controller.players
                                        )
        self.report_management = ReportManagement(self.player_controller,
                                                  self.tournament_controller
                                                  )
        self.filename = r'\db.json'
        db_exist = os.path.exists(self.filename)
        if db_exist is not True:
            self.db = self.tools.create_db()
        else:
            self.db = self.filename
        self.players_table = self.db.table('Players')
        self.tournaments_table = self.db.table('Tournaments')

    def run(self):
        """Run the menu option"""
        menu = {
            "1": self.tournament_controller.new_tournament,
            "2": self.player_controller.create_player,
            "3": self.tournament_controller.add_player,
            "4": self.tournament_controller.create_a_round,
            "5": self.tournament_controller.play_a_round,
            "6": self.tournament_controller.update_player_ranking,
            "7": self.report_management.choose_a_report,
            "8": self.save_function,
            "9": self.load_function,
            "10": self.stop_game
                }

        while self.active:
            choice = self.menu_view.prompt_menu_choice()
            if choice in menu:
                menu[choice]()
            else:
                print("invalid option")
        print("Thanks and have a good day!")

    def save_function(self):
        # empty tables
        self.players_table.truncate()
        self.tournaments_table.truncate()
        # save function for players
        players = self.player_controller.players
        for player in players:
            serialize_player = player.serialize()
            self.players_table.insert(serialize_player)
        # save function for tournaments
        tournaments_list = self.tournament_controller.tournaments_list
        for tournament in tournaments_list:
            serialize_tournament = tournament.serialize(
                self.tournament_controller.players_all
                )
            self.tournaments_table.insert(serialize_tournament)

    def load_function(self):
        # Build-on the Players List with the Players table
        players_list = self.players_table.all()
        for player in players_list:
            self.player_controller.load_player_from_bd(player)
        # Build-on the Tournaments List with the Tournaments table
        tournaments_list = self.tournaments_table.all()
        for tournament in tournaments_list:
            self.tournament_controller.load_tournament_from_bd(tournament)

    def stop_game(self):
        self.active = False
