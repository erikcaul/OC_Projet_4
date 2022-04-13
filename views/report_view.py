"""Report view"""


class ReportView:
    
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
            player.print_player()
    
    def print_tournament_report(self, tournaments_list): 
        for tournament in tournaments_list:
            tournament.print_tournament()
    
    def print_rounds_report(self, rounds_list): 
        for round in rounds_list:
            round.print_round()

    def print_games_report(self, games_list): 
        for game in games_list:
            game.print_game()