"""Report view"""
import json
from views.player_view import PlayerView
from views.tournament_view import TournamentView



class ReportView:
    def __init__(self):
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()


    def prompt_report_choice(self):
        """ Prompt for a report to choice"""
        print("---------------------------------------------------")
        print("---------------------------------------------------")
        print("Choose a report : \n"
              "1. All players list report by alphabetical order\n"
              "2. All players list report by ranking\n"
              "3. Tournament players list report by alphabetical order\n"
              "4. Tournament players list report by ranking\n"
              "5. All tournaments list\n"
              "6. All rounds tournament list\n"
              "7. All games tournament list\n"
              "8. Quit\n")
        print("---------------------------------------------------")
        choice = input('Enter your choice between 1 and 8 : \n')
        return choice


    def print_players_report(self, players_list):
        for player in players_list:
            self.player_view.print_player(player)

    def print_tournament_report(self, tournaments_list):
        for tournament in tournaments_list:
            self.tournament_view.print_tournament(tournament)

    def print_rounds_report(self, rounds_list):
        for round in rounds_list:
            # round_d = json.load(round)
            self.tournament_view.print_round(round)

    def print_games_report(self, games_list):
        for game in games_list:
            self.tournament_view.print_game(game)
