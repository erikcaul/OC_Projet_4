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


    def print_players_report(self, players_list): # deonner plus de détail - Player 1 : nom, prénom, score, etc. avec des séparateurs
        for player in players_list:
            player_dict = player.serialize_player(player)
            print(player_dict)
            print("---------------------------------------------------")
    
    def print_tournament_report(self, tournaments_list): # donner les info principales nom date, type , nombre rounds max, etc.info que je rentre quand fais le tournois
        for tournament in tournaments_list:
            tournament_dict = tournament.serialize_tournament(tournament)
            print(tournament_dict)
            print("---------------------------------------------------")
    
    def print_rounds_report(self, rounds_list): # rajouter des séparateurs
        for round in rounds_list:
            round_dict = round.serialize_round(round)
            print(round_dict)
            print("---------------------------------------------------")

    def print_games_report(self, games_list): # rajouter des séparateurs
        i = 1
        for game in games_list:
            print("Game " + str(i) + " : ")
            game_dict = game.serialize_game(game)
            print(game_dict)
            print("---------------------------------------------------")
            i += 1