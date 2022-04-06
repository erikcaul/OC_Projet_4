class Game:
    """Patern for a game"""
    def __init__(self, player_1, player_2, begin_date):
        """Initialize a game"""
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_win = None
        self.player_2_win = None
        self.begin_date = begin_date
        self.end_date = None

    def print_game(self, game):
        print("---------------------------------------------------")
        print("Player 1 : ") 
        game.player_1.print_player(game.player_1)
        print("Player 2 : ")
        game.player_2.print_player(game.player_2)
        print("Player 1 win ? : " + str(game.player_1_win))
        print("Player 2 win ? : " + str(game.player_2_win))
        print("Game begin date : " + str(game.begin_date))
        print("Game end date : " + str(game.end_date))
        print("---------------------------------------------------")
    
    def dict_game(self, game):
        game_dict = {}
        game_dict["Player 1 name"] = game.player_1.dict_player(game.player_1)
        game_dict["Player 2 name"] = game.player_2.dict_player(game.player_2)
        game_dict["Player 1 win"] = game.player_1_win
        game_dict["Player 2 win"] = game.player_2_win
        game_dict["Game begin date"] = game.begin_date
        game_dict["Game end date"] = game.end_date     
        return game_dict