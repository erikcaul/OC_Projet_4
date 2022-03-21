
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

    def pick_up_tournament(self, list):
        """prompt to pick-up a tournament"""
        print('Tournaments names : ')
        menu_instance = self.tools.print_name_list(list)
        tournament_choice = input('Choice the tournament: ')
        pick_up_tournament = self.tools.validate_menu_choice(tournament_choice, menu_instance, list)
        return pick_up_tournament

    def pick_up_player(self, all_players_list, tournament_players_list):
        """prompt to pick-up a player"""
        print('Players names : ')
        filtered_players_list = []
        for player in all_players_list:
            if player not in tournament_players_list:
                filtered_players_list.append(player)
        menu_instance = self.tools.print_name_list(filtered_players_list)
        player_choice = input('Choice the player: ')
        pick_up_player = self.tools.validate_menu_choice(player_choice, menu_instance, filtered_players_list)
        return pick_up_player

    def prompt_games_results(self, game):
        # add the 2 players in a list
        game_players_list = [game.player_1, game.player_2]
        # pick_up_player for the winner
        # game_result = self.tournament_view.pick_up_player(self.players_all, game_players_list)
        self.tools.print_name_list(game_players_list)
        winner = input('Please enter the number of the winner (0 if none) : \n')
        return winner
