"""Tournament view"""
from multiprocessing.sharedctypes import Value
from models.tournament import Tournament

class TournamentView:
    def __init__(self):
        pass

    def prompt_tournament_creation(self):
        """prompt info for the creation of a tournament"""
        # faire un dict plutôt qu'une liste avec initialisation à vide
        tournament_dict = {
            "name": input('Enter the tournament name : '),
            "location": input('Enter the location of the tournament : '),
            "date": input('Enter the date of the tournament : '),
            "turns_number": input('Enter the number of turns for the tournament : '),
            "time_controller": input('Please select the type for the time controlling (1. bullet, 2. blitz, 3. quick hit) : '),
            "description": input('Please enter a description for the tournament: ')
        }

        for key in tournament_dict:
            value = tournament_dict[key]
            for value in tournament_dict:
                if value in tournament_dict:
                    if value != "":
                        tournament_dict[key] = value
                else: 
                    tournament_dict()
                
            
            
        
        # valider ce qui rentre (ne pas accepter qu'il ne rentre rien du tout et n'accepter que les 3 types prévus, et nombres de tours, dates, etc. avec un retry)
        # fonction d'input avec validation
        
        return tournament_dict


    def prompt_add_player(self):
        """prompt for adding player to a tournament"""
        # récupérer la lste des players et la liste des tournaments
        # afficher liste tournois 1 ... n et demande de choisir  quel tourois, pareil pour players qui sont pas encore dans tournoi
        tournament_name = input('Please indicate the name of the tournament for which you want to add a player : ')
        player_name = input("Please indicate the player's name you want to add to the tournament : ")
        

    
