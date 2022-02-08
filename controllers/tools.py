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
        i = 1
        for instance in instance_list:
            print(str(i) + '. ' + instance.name)
            i += 1
        input('')

    def pick_up_player(self, instance_list):
        """prompt to pick-up a player"""
        print('Players names : ')
        i = 1
        for instance in instance_list:
            print(str(i) + '. ' + instance.family_name)
            i += 1