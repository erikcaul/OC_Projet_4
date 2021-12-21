"""main loop controleur : user chooses between options"""
from models import player, tournament, game, round

"""Un contrôleur qui va faire main loop (choix option), 
avant le choix, va appeler la vue "menu" pour afficher les options et ensuite attendre input 
Use an infinite loop to show the menu options.
Ask the user for the options
Use if-elif-else to determine what to do according to the user input. """

class main_loop:
    def __init__(self, menu_view):
        self.menu_view = menu_view
    # Infinite loop
    run = True
    while(run):
        # afficher menu options
        option = int(input('Enter your choice: '))

