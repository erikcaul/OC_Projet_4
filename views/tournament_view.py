
"""Tournament view"""
from controllers.tools import Tools


class TournamentView:
    def __init__(self):
        self.tools = Tools()
        self.time_controller_list = ['bullet',
            'blitz',
            'quick hit'] 

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

        tournament_info = {}
        for key, value in tournament_dict.items(): 
            user_input = None
            while user_input == "" or user_input == None:
                user_input = input(value)
                tournament_info[key] = user_input
            if key == 'date':
                while not self.tools.validate_date(user_input):
                    user_input = input(value)
                    tournament_info[key] = user_input
            if key == 'turns_number':
                while not self.tools.validate_number(user_input): 
                    user_input = input(value)
                    tournament_info[key] = user_input
            if key == 'time_controller':
                while not self.tools.validate_list(user_input, self.time_controller_list):
                    user_input = input(value)
                    tournament_info[key] = user_input        
        return tournament_info

    # pick-up instance de tournament ou de player (pas trop générique faire pour chacun d'eux)
    # ne pas porposer un joueur qui est déjà dans le tournoi
    def pick_up_tournament(self, list):
        """prompt to pick-up a tournament"""
        print('Tournaments names : ')
        menu_instance = {}
        menu_instance = self.tools.print_choice_list(list, menu_instance)
        tournament_choice = input('Choice the tournament: ')
        pick_up_tournament = self.tools.validate_menu_choice(tournament_choice, menu_instance, list)
        return pick_up_tournament

    def pick_up_player(self, list):
        """prompt to pick-up a player"""
        print('Players names : ')
        menu_instance = {}
        menu_instance = self.tools.print_choice_list(list, menu_instance)
        tournament_choice = input('Choice the player: ')
        pick_up_player = self.tools.validate_menu_choice(tournament_choice, menu_instance, list)
        return pick_up_player

        # afficher liste tournois 1 ... n et demande de choisir  quel tourois, pareil pour players qui sont pas encore dans tournoi
        # tournament_name = input('Please indicate the name of the tournament for which you want to add a player : ')
        # player_name = input("Please indicate the player's name you want to add to the tournament : ")