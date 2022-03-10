class Tournament:
    """Patern for tournaments"""
    def __init__(self, name, location, date, rounds, players, players_ranking, time_controller, turns_number=4, description=""):
        """initialize tournament"""
        self.name = name
        self.location = location
        self.date = date
        self.rounds = rounds
        self.players = players
        self.players_ranking = players_ranking # (commence à 0) nombre de point par joueur pour le tournois (dict[instance joueur] = nombre de points)
        self.time_controller = time_controller
        self.turns_number = turns_number
        self.description = description
