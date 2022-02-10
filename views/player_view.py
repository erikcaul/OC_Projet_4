from controllers.tools import Tools


"""Player view"""

class PlayerView:
    def __init__(self):
        self.tools = Tools()
        self.sexe_list = ['female',
            'male',
            'not saying'] 

    def prompt_player_creation(self):
        """prompt info for the creation of a player"""
        # faire un dict plutôt qu'une liste avec initialisation à vide
        player_dict = {
            "family_name": 'Enter the player family name : ',
            "first_name": 'Enter the player first name : ',
            "birth_date": 'Enter the birth date of the player with DDMMYYYY format: ',
            "sexe": 'Please select the sexe of the player (male, female, not binary) : ',
            "ranking": 'Please enter the player ranking : '
            }
        
        player_info = {}
        for key, value in player_dict.items(): 
            user_input = None
            while user_input == "" or user_input == None:
                user_input = input(value)
                player_info[key] = user_input
            if key == 'birth_date':
                while not self.tools.validate_date(user_input):
                    user_input = input(value)
                    player_info[key] = user_input
            if key == 'ranking':
                while not self.tools.validate_number(user_input): 
                    user_input = input(value)
                    player_info[key] = user_input
            if key == 'sexe':
                while not self.tools.validate_list(user_input, self.sexe_list):
                    user_input = input(value)
                    player_info[key] = user_input        
        return player_info

    
