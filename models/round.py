class Round:
    """Patern for a round"""
    def __init__(self, round_name, games, begin_date):
        """Initialize a round"""
        self.round_name = round_name
        self.games = games
        self.begin_date = begin_date
        self.end_date = None

    def serialize_round(self, round):
        round_dict = {}
        round_dict["Round name"] = round.round_name
        round_dict["Round games"] = []
        for game in round.games:
            game_serialize = game.serialize_game(game)
            round_dict["Round games"].append(game_serialize)
        round_dict["Begin date"] = game.begin_date
        round_dict["End date"] = game.end_date  
        return round_dict