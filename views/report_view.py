"""Report view"""


class ReportView:
    
    def prompt_report_choice(self):
        """ Prompt for a report to choice"""
        print("Choose a report : \n"
              "1. All players list report by alphabetical order\n"
              "2. All players list report by ranking\n"
              "3. Tournament players list report by alphabetical order\n"
              "4. Tournament players list report by ranking\n"
              "5. All tournaments list\n"
              "6. All rounds tournament list\n"
              "7. All games tournament list\n"
              "8. Quit\n")
        choice = input('Enter your choice between 1 and 8 : \n')
        return choice


    def print_players_report(self, players_list):
        for player in players_list:
            print(player.name + " : " + player.ranking)
    
    def print_tournament_report(self, tournaments_list):
        for tournament in tournaments_list:
            print(tournament.name)

    def print_rounds_report(self, rounds_list):
        for round in rounds_list:
            print(round.round_name)
            print(round.games)
            print(round.begin_date)
            print(round.end_date + "\n")

    def print_games_report(self, games_list):
        i = 1
        for game in games_list:
            print("Game " + i + " : \n")
            print(game.player_1)
            print(game.player_2)
            print(game.player_1_win)
            print(game.player_2_win)
            print(game.begin_date)
            print(game.end_date + "\n")
            i += 1