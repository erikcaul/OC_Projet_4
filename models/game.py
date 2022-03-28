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
