# import time

class Round:
    """Patern for a round"""
    def __init__(self, round_name, games, begin_date, end_date=None):
        """Initialize a round"""
        self.round_name = round_name
        self.games = games
        self.begin_date = begin_date
        self.end_date = end_date

    def print_round(self): # à mettre dans report_view
        print("---------------------------------------------------")
        print("---------------------------------------------------")
        print("---Round name : " + str(self.round_name))
        print("---Round games : ")
        i = 1
        for game in self.games:
            print("   ---Game " + str(i) + " : ")
            game.print_game()
            i += 1
        print("---Round begin date : " + str(self.begin_date))
        print("---Round end date : " + str(self.end_date))
        print("---------------------------------------------------")
        print("---------------------------------------------------")

    def serialize(self, all_players_list):
        games_list = []
        for game in self.games:
            game_serialize = game.serialize(all_players_list)
            games_list.append(game_serialize)
        return {
            "round_name": self.round_name,
            "games": games_list,
            "begin_date": self.begin_date,
            "end_date": self.end_date
        }

    