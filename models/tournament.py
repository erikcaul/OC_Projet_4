class Tournament:
    """Patern for tournaments"""
    def __init__(self, name, place, date, rounds, players, time_controller, tunrs_number=4, description=""):
        """initialize tournament"""
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.players = players
        self.time_controller = time_controller
        self.turns_number = tunrs_number
        self.description = description

   
