"""Tournament view"""
from models.tournament import Tournament

class TournamentView:
    def __init__(self):
        pass

    def prompt_tournament_creation(self):
        """prompt info for the creation of a tournament"""
        # faire un dict plutôt qu'une liste avec initialisation à vide
        # valider ce qui rentre (ne pas accepter qu'il ne rentre irne du tout et n'accpeter que les 3 types prévus, et nombres de tours, dates, etc. avec un retry)
        # fonction d'input avec validation
        tournament_info = ['name', 'location', 'date', 0, 'bullet', 'description']
        tournament_info[0] = input('Enter the tournament name : ')
        tournament_info[1] = input('Enter the location of the tournament : ')
        tournament_info[2] = input('Enter the date of the tournament : ')
        tournament_info[3] = input('Enter the number of turns for the tournament : ')
        tournament_info[4] = input('Please select the type for the time controlling (1. bullet, 2. blitz, 3. quick hit) : ')
        tournament_info[5] = input('Please enter a description for the tournament: ')
        return tournament_info


    def prompt_add_player(self):
        """prompt for adding player to a tournament"""
        # récupérer la lste des players et la liste des tournaments
        # afficher liste tournois 1 ... n et demande de choisir  quel tourois, pareil pour players qui sont pas encore dans tournoi
        tournament_name = input('Please indicate the name of the tournament for which you want to add a player : ')
        player_name = input("Please indicate the player's name you want to add to the tournament : ")
        

    
