from datetime import datetime

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

    def pick_up_tournament(self, instance_list):
        """prompt to pick-up a tournament"""
        print('Tournaments names : ')
        menu_instance = {}
        i = 1
        for instance in instance_list:
                menu_instance[str(i)] = instance.name 
                print(str(i) + '. ' + instance.name)
                i += 1
        good_choice = True
        while good_choice:
            tournament_choice = input('Choice the tournament: ')
            if tournament_choice in menu_instance:
                number_in_list = int(tournament_choice) - 1 
                pick_up_tournament = instance_list[number_in_list]
                good_choice = False
            else:
                print("invalid option")        
        return pick_up_tournament

    def pick_up_player(self, instance_list):
        """prompt to pick-up a player"""
        print('Players names : ')
        menu_instance = {}
        i = 1
        for instance in instance_list:
                menu_instance[str(i)] = instance.family_name 
                print(str(i) + '. ' + instance.family_name)
                i += 1
        good_choice = True
        while good_choice:
            player_choice = input('Choice the player to add to tournament choiced: ')
            if player_choice in menu_instance:
                number_in_list = int(player_choice) - 1 
                pick_up_player = instance_list[number_in_list]
                good_choice = False
            else:
                print("invalid option")          
        return pick_up_player
        