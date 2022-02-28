class Player:
    """Patern for a player"""
    def __init__(self, family_name, first_name, birth_date, sexe, ranking):
        """initialize player"""
        self.name = family_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sexe = sexe
        self.ranking = ranking # nombre de points

    