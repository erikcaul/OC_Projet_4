"""main loop controller : user chooses between options"""
from controlers import create_tournament
from models import tournament, player

"""Un contrôleur qui va faire main loop (choix option), 
avant le choix, va appeler la vue "menu" pour afficher les options et ensuite attendre input 
Use an infinite loop to show the menu options.
Ask the user for the options
Use if-elif-else to determine what to do according to the user input. """


class MainLoop:
    def __init__(self, menu_view, active="True"):
        self.menu_view = menu_view
        self.active = active

    def run(self):
        """Run the menu option"""
        while self.active:
            choice = self.menu_view.prompt_menu_choice(self)
            if choice == 1:
                create_tournament.CreateTournament.new_tournament(self)
            elif choice == 2:
                player.create_player(self)
            elif choice == 3:
                tournament.add_player(self)
            elif choice == 4:
                print("Thanks and have a good day!")
                active = False
                return active
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
