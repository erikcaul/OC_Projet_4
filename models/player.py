class Player:
    """Patern for a player"""
    def __init__(self, family_name, first_name, birth_date, sexe, ranking):
        """initialize player"""
        self.name = family_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sexe = sexe
        self.ranking = ranking # nombre de points

    def serialize_player(self, player):
        player_dict = {}
        player_dict["Player family name"] = player.name
        player_dict["Player first name"] = player.first_name
        player_dict["Player birth date"] = player.birth_date     
        player_dict["Player sexe"] = player.sexe
        player_dict["Player ranking"] = player.ranking    
        return player_dict
