"""main loop controller : user chooses between options"""
from controllers import player_controller, tournement_controller
from models import tournament
from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournement_controller import TournamentController


"""Un contrôleur qui va faire main loop (choix option), 
avant le choix, va appeler la vue "menu" pour afficher les options et ensuite attendre input 
Use an infinite loop to show the menu options.
Ask the user for the options
Use if-elif-else to determine what to do according to the user input. """


class MainLoop:
    def __init__(self, menu_view, active="True"):
        self.menu_view = MenuView()
        self.active = active
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController

    def run(self):
        """Run the menu option"""
        while self.active:
            choice = self.menu_view.prompt_menu_choice(self)
            if choice == 1:
                tournement_controller.new_tournament()
            elif choice == 2:
                player_controller.create_player()
            elif choice == 3:
                tournement_controller.add_player()
            elif choice == 4:
                print("Thanks and have a good day!")
                active = False
                return active
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
