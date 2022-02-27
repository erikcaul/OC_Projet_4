from datetime import datetime
import operator

"""tools module"""

class Tools:
    def __init__(self):
        pass


    def validate_date(self, date_string):
        format = "%d%m%Y"
        try:
            datetime.strptime(date_string, format)
            return True

        except:
            print("This is the incorrect date string format. It should be DDMMYYYY")
            return False

    def validate_number(self, number_string):
        try:
            number_string = int(number_string)
            isinstance(number_string, str)
            return True

        except:
            return False

    def validate_list(self, user_input, elements_list):
        try:
            for componant in elements_list:
                if componant == user_input:
                    return True
        except:
            return False

    def print_name_list(self, list):
        menu_instance = {}
        i = 1
        for element in list:
                menu_instance[str(i)] = element.name
                print(str(i) + '. ' + element.name)
                i += 1
        return menu_instance

    def validate_menu_choice(self, choice, menu, list):
        try:
            if choice in menu:
                number_in_list = int(choice) - 1
                pick_up_element = list[number_in_list]
                return pick_up_element
        except:
            print("invalid option")

    def match_making(self, tournament):
        # Au début du premier tour, triez tous les joueurs en fonction de leur classement.
        # trier tous les joueurs en fonction de leur classement
        tournament_players = tournament.players
        ranking_dict = {}
        for player in tournament_players:
            player_name = player.name
            player_ranking = player.ranking
            ranking_dict[player_name] = player_ranking
        print(ranking_dict)
        sorted_ranking_list = sorted(ranking_dict.items(), key=operator.itemgetter(1))
        print(sorted_ranking_list)

        # Divisez les joueurs en deux moitiés, une supérieure et une inférieure.
        half = len(sorted_ranking_list)//2
        list1 = sorted_ranking_list[:half]
        list2 = sorted_ranking_list[half:]
        print(list1)
        print(list2)
        # Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur joueur de la moitié inférieure,
        # et ainsi de suite.
        # Si nous avons huit joueurs triés par rang, alors le joueur 1 est jumelé avec le joueur 5, le joueur 2 est jumelé avec le joueur 6, etc.
        round1 = {}
        i = 0
        for element1 in list1:
            round1[i+1] = (element1[0], list2[i][0])
            i+=1
        print(round1)
        return round1
        # Au prochain tour, triez tous les joueurs en fonction de leur nombre total de points.

        # Si plusieurs joueurs ont le même nombre de points, triez-les en fonction de leur rang.
        # Associez le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4, et ainsi de suite. Si le joueur 1 a déjà joué contre le joueur 2, associez-le plutôt au joueur 3.
        # Répétez les étapes 3 et 4 jusqu'à ce que le tournoi soit terminé.
