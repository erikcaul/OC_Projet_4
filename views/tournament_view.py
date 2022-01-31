from datetime import datetime

"""Tournament view"""

class TournamentView:
    def __init__(self):
        self.time_controller_list = ['bullet',
            'blitz',
            'quick hit'] 
    
    def validate_date(self, date_string):
        format = "%d%m%Y"
        try:
            datetime.strptime(date_string, format)
            return True
            
        except:
            print("This is the incorrect date string format. It should be DDMMYYYY")
            return False

    def validate_number(self, number_string):
        try:
            number_string = int(number_string)
            isinstance(number_string, str)
            return True

        except:
            return False

    def validate_list(self, list_string):
        try:
            for componant in self.time_controller_list:
                if componant == list_string:
                    return True
        except:
            return False

    def prompt_tournament_creation(self):
        """prompt info for the creation of a tournament"""
        # faire un dict plutôt qu'une liste avec initialisation à vide
        tournament_dict = {
            "name": 'Enter the tournament name : ',
            "location": 'Enter the location of the tournament : ',
            "date": 'Enter the date of the tournament with DDMMYYYY format: ',
            "turns_number": 'Enter the number of turns for the tournament : ',
            "time_controller": 'Please select the type for the time controlling (bullet, blitz, quick hit) : ',
            "description": 'Please enter a description for the tournament: '
        }
        for key, value in tournament_dict.items(): 
            user_input = None
            while user_input == "" or user_input == None:
                user_input = input(value)
            if key == 'date':
                while not self.validate_date(user_input) :
                    user_input = input(value)
            if key == 'turns_number':
                while not self.validate_number(user_input): 
                    user_input = input(value)
            if key == 'time_controller':
                while not self.validate_list(user_input):
                    user_input = input(value)        
        return tournament_dict


    def prompt_add_player(self):
        """prompt for adding player to a tournament"""
        # récupérer la lste des players et la liste des tournaments
        # afficher liste tournois 1 ... n et demande de choisir  quel tourois, pareil pour players qui sont pas encore dans tournoi
        tournament_name = input('Please indicate the name of the tournament for which you want to add a player : ')
        player_name = input("Please indicate the player's name you want to add to the tournament : ")