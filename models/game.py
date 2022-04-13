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

    def print_game(self): # à mettre dans report_view
        print("---------------------------------------------------")
        print("------Player 1 : ") 
        self.player_1.print_player()
        print("------Player 2 : ")
        self.player_2.print_player()
        print("   ------Player 1 win ? : " + str(self.player_1_win))
        print("   ------Player 2 win ? : " + str(self.player_2_win))
        print("   ------Game begin date : " + str(self.begin_date))
        print("   ------Game end date : " + str(self.end_date))
        print("---------------------------------------------------")

    def serialize(self):
        return {
            "player_1": self.player_1.serialize(),
            "player_2": self.player_2.serialize(),
            "player_1_win": self.player_1_win,
            "player_2_win": self.player_2_win,
            "begin_date": self.begin_date,
            "end_date": self.end_date
        }