import time

class Round:
    """Patern for a round"""
    def __init__(self, round_name, games, begin_date):
        """Initialize a round"""
        self.round_name = round_name
        self.games = games
        self.begin_date = begin_date
        self.end_date = None

    def print_round(self, round):
        print("---------------------------------------------------")
        print("Round name : " + str(round.round_name))
        print("Round games : ")
        i = 1
        for game in round.games:
            print("Game " + str(i) + " : ")
            game.print_game(game)
            i += 1
        print("Round begin date : " + str(self.begin_date))
        print("Round end date : " + str(self.end_date))
        print("---------------------------------------------------")
    
    def dict_round(self, round):
        round_dict = {}
        round_dict["Round name"] = round.round_name
        round_dict["Round games"] = []
        for game in round.games:
            game_dict = game.dict_game(game)
            round_dict["Round games"].append(game_dict)
        round_dict["Begin date"] = game.begin_date
        round_dict["End date"] = game.end_date  
        return round_dict