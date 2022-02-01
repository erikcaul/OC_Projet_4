from datetime import datetime


"""Player view"""

class PlayerView:
    def __init__(self):
        self.sexe_list = ['female',
            'male',
            'not saying'] 

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
            if number_string > 0:
                return True

        except:
            return False

    def validate_list(self, list_string):
        try:
            for componant in self.sexe_list:
                if componant == list_string:
                    return True
        except:
            return False

    def prompt_player_creation(self):
        """prompt info for the creation of a player"""
        # faire un dict plutôt qu'une liste avec initialisation à vide
        player_dict = {
            "family_name": 'Enter the player family name : ',
            "first_name": 'Enter the player first name : ',
            "birth_date": 'Enter the birth date of the player with DDMMYYYY format: ',
            "sexe": 'Please select the sexe of the player (male, female, not saying) : ',
            "ranking": 'Please enter the player ranking : '
            }
        for key, value in player_dict.items(): 
            user_input = None
            while user_input == "" or user_input == None:
                user_input = input(value)
            if key == 'birth_date':
                while not self.validate_date(user_input) :
                    user_input = input(value)
            if key == 'ranking':
                while not self.validate_number(user_input): 
                    user_input = input(value)
            if key == 'sexe':
                while not self.validate_list(user_input):
                    user_input = input(value)        
        return player_dict
