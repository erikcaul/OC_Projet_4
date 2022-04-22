class Player:
    """Patern for a player"""
    def __init__(self, name, first_name, birth_date, sexe, ranking):
        """initialize player"""
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sexe = sexe
        self.ranking = ranking # nombre de points
        
    def serialize(self):
        return {
            "name": self.name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "sexe": self.sexe,
            "ranking": self.ranking
        }
