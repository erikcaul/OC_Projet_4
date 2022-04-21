class Player:
    """Patern for a player"""
    def __init__(self, name, first_name, birth_date, sexe, ranking):
        """initialize player"""
        self.name = name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sexe = sexe
        self.ranking = ranking # nombre de points
        
    def print_player(self): # à mettre dans report_view
        print("---------------------------------------------------")
        print("---Player family name : " + str(self.name))
        print("---Player first name : " + str(self.first_name))
        print("---Player birth date : " + str(self.birth_date))
        print("---Player sexe : " + str(self.sexe))
        print("---Player ranking : " + str(self.ranking))
        print("---------------------------------------------------")

    def serialize(self):
        return {
            "name": self.name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "sexe": self.sexe,
            "ranking": self.ranking
        }