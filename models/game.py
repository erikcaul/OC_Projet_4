class Game:
    """Patern for a game"""
    def __init__(self, player_1, player_2, begin_date, player_1_win=None, player_2_win=None, end_date=None):
        """Initialize a game"""
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1_win = player_1_win
        self.player_2_win = player_2_win
        self.begin_date = begin_date
        self.end_date = end_date

    def serialize(self, all_players_list):
        return {
            "player_1": all_players_list.index(self.player_1),
            "player_2": all_players_list.index(self.player_2),
            "player_1_win": self.player_1_win,
            "player_2_win": self.player_2_win,
            "begin_date": self.begin_date,
            "end_date": self.end_date
        }
