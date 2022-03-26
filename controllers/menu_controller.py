"""main loop controller : user chooses between options"""

from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_management import ReportManagement


"""Un contrôleur qui va faire main loop (choix option),
avant le choix, va appeler la vue "menu" pour afficher les options et ensuite attendre input
Use an infinite loop to show the menu options.
Ask the user for the options
Use if-elif-else to determine what to do according to the user input. """


class MainLoop:
    def __init__(self, menu_view, active=True):
        self.menu_view = MenuView()
        self.active = active
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController(self.player_controller.players)
        self.report_management = ReportManagement(self)


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
            "8": self.stop_game
        }

        while self.active:
            choice = self.menu_view.prompt_menu_choice()
            if choice in menu:
                menu[choice]()
            else:
                print("invalid option")

        print("Thanks and have a good day!")

    def stop_game(self):
        self.active = False
