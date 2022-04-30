from datetime import datetime
from tinydb import TinyDB


"""tools module"""


class Tools:
    def __init__(self):
        self.db = self.create_db()

    def create_db(self):
        db = TinyDB('db.json')
        return db

    def validate_date(self, date_string):
        format = "%d%m%Y"
        try:
            datetime.strptime(date_string, format)
            return True

        except format is not True:
            print("This is the incorrect date string format."
                  "It should be DDMMYYYY"
                  )
            return False

    def validate_number(self, number_string):
        try:
            number_string = int(number_string)
            isinstance(number_string, str)
            return True

        except isinstance(number_string, str) is not True:
            return False

    def validate_list(self, user_input, elements_list):
        try:
            for componant in elements_list:
                if componant == user_input:
                    return True
        except componant not in elements_list:
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
        except choice not in menu:
            print("invalid option")
