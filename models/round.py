class Round:
    """Patern for a round"""
    def __init__(self, round_name, games, begin_date):
        """Initialize a round"""
        self.round_name = round_name
        self.games = games
        self.begin_date = begin_date
        self.end_date = None
