"""Tournament view"""
from multiprocessing.sharedctypes import Value
from unicodedata import digit
from models.tournament import Tournament

class TournamentView:
    def __init__(self):
        pass

    def prompt_tournament_creation(self):
        """prompt info for the creation of a tournament"""
        # faire un dict plutôt qu'une liste avec initialisation à vide
        tournament_dict = {
            "name": 'Enter the tournament name : ',
            "location": 'Enter the location of the tournament : ',
            "date": 'Enter the date of the tournament : ',
            "turns_number": 'Enter the number of turns for the tournament : ',
            "time_controller": 'Please select the type for the time controlling (bullet, blitz, quick hit) : ',
            "description": 'Please enter a description for the tournament: '
        }
        tournament_info = {}
        for key, value in tournament_dict.items():
            user_input = None
            while user_input == "" or user_input == None:
                user_input = input(value)
            while key == 'date' and user_input is digit : # vérifier simplement DDMMYYYY
                user_input = input(value)
                print('cle, valeur\n', key, user_input, "\n")
            if isinstance(user_input, str): # dans un while pour turn_numbers
                user_input = int(user_input)
            while key == 'turns_number' and user_input > 4: # toujours un str donc convertir en nombre
                user_input = input(value)
                print('cle, valeur\n', key, user_input, "\n")
            while key == 'time_controller' and (user_input > 0 and user_input < 4): # valider Bullet, blitz and quick hit putôt que des int (list avec toutes les valeurs dont user_input doit être in the list)
                user_input = input(value)
                print('cle, valeur\n', key, user_input, "\n")
            
        # valider ce qui rentre (ne pas accepter qu'il ne rentre rien du tout et n'accepter que les 3 types prévus, et nombres de tours, dates, etc. avec un retry)
        # fonction d'input avec validation
        
        return tournament_info


    def prompt_add_player(self):
        """prompt for adding player to a tournament"""
        # récupérer la lste des players et la liste des tournaments
        # afficher liste tournois 1 ... n et demande de choisir  quel tourois, pareil pour players qui sont pas encore dans tournoi
        tournament_name = input('Please indicate the name of the tournament for which you want to add a player : ')
        player_name = input("Please indicate the player's name you want to add to the tournament : ")