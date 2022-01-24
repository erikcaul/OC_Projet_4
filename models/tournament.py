class Tournament:
    """Patern for tournaments"""
    def __init__(self, name, location, date, rounds, players, time_controller, tunrs_number=4, description=""):
        """initialize tournament"""
        self.name = name
        self.location = location
        self.date = date
        self.rounds = rounds
        self.players = players
        self.time_controller = time_controller
        self.turns_number = tunrs_number
        self.description = description