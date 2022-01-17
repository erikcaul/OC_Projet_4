"""Menu view"""


class MenuView:
    """Main menu"""

    def prompt_menu_choice(self):
        """Prompt for a choice"""
        print("Choose an option : \n"
              "1. Create a tournament\n"
              "2. Create a player\n"
              "3. Add a player to a tournament\n"
              "4. Quit\n")
        choice = input('Enter your choice between 1 and 4 : \n')
        return choice
