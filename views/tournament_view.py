"""Tournament view"""
from controllers.tools import Tools
from views.player_view import PlayerView


class TournamentView:
    def __init__(self):
        self.player_view = PlayerView()
        self.tools = Tools()
        self.time_controller_list = ['bullet',
                                     'blitz',
                                     'quick hit'
                                     ]

    def prompt_tournament_creation(self):
        """prompt info for the creation of a tournament"""
        # faire un dict plutôt qu'une liste avec initialisation à vide
        tournament_dict = {
            "name": 'Enter the tournament name : ',
            "location": 'Enter the location of the tournament : ',
            "date": 'Enter the date of the tournament with DDMMYYYY format: ',
            "turns_number": 'Enter the number of turns for the tournament : ',
            "time_controller": 'Please select the time controlling type'
                               '(bullet, blitz, quick hit) : ',
            "description": 'Please enter a description for the tournament: ',
        }

        tournament_info = {}
        for key, value in tournament_dict.items():
            user_input = None
            while user_input == "" or user_input is None:
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
                while not self.tools.validate_list(user_input,
                                                   self.time_controller_list
                                                   ):
                    user_input = input(value)
                    tournament_info[key] = user_input
        return tournament_info

    def pick_up_tournament(self, list):
        """prompt to pick-up a tournament"""
        print('Tournaments names : ')
        menu_instance = self.tools.print_name_list(list)
        tournament_choice = input('Choice the tournament: ')
        pick_up_tournament = self.tools.validate_menu_choice(
                                        tournament_choice,
                                        menu_instance,
                                        list
                                        )
        return pick_up_tournament

    def pick_up_player(self, all_players_list, tournament_players_list):
        """prompt to pick-up a player"""
        print('Players names : ')
        filtered_players_list = []
        for player in all_players_list:
            if player not in tournament_players_list:
                filtered_players_list.append(player)
        if len(filtered_players_list) != 0:
            menu_instance = self.tools.print_name_list(filtered_players_list)
            player_choice = input('Choice the player: ')
            pick_up_player = self.tools.validate_menu_choice(
                                        player_choice,
                                        menu_instance,
                                        filtered_players_list
                                        )
            return pick_up_player

    def prompt_games_results(self, game):
        # add the 2 players in a list
        game_players_list = [game.player_1, game.player_2]
        # pick_up_player for the winner
        self.tools.print_name_list(game_players_list)
        winner = input('Please enter the winner number (0 if none) : \n')
        return winner

    def print_tournament(self, tournament):
        print("---------------------------------------------------")
        print("Tournament name : " + str(tournament.name))
        print("Tournament location : " + str(tournament.location))
        print("Tournament date : " + str(tournament.date))
        print("Tournament time controller : " + str(
                                                tournament.time_controller
                                                ))
        print("Tournament turns number : " + str(tournament.turns_number))
        print("Tournament description : " + str(tournament.description))
        print("---------------------------------------------------")

    def print_round(self, round):
        print("---------------------------------------------------")
        print("---------------------------------------------------")
        print("---Round name : " + str(round.round_name))
        print("---Round games : ")
        i = 1
        for game in round.games:
            print("   ---Game " + str(i) + " : ")
            self.print_game(game)
            i += 1
        print("---Round begin date : " + str(round.begin_date))
        print("---Round end date : " + str(round.end_date))
        print("---------------------------------------------------")
        print("---------------------------------------------------")

    def print_game(self, game):
        print("---------------------------------------------------")
        print("------Player 1 : ")
        self.player_view.print_player(game.player_1)
        print("------Player 2 : ")
        self.player_view.print_player(game.player_2)
        print("   ------Player 1 win ? : " + str(game.player_1_win))
        print("   ------Player 2 win ? : " + str(game.player_2_win))
        print("   ------Game begin date : " + str(game.begin_date))
        print("   ------Game end date : " + str(game.end_date))
        print("---------------------------------------------------")
