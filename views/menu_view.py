"""Menu view"""


class MenuView:
    """Main menu"""

    def prompt_menu_choice(self):
        """Prompt for a choice"""
        print("Choose an option : "
              "1. Create a tournament"
              "2. Create a player"
              "3. Add a player to a tournament"
              "4. Quit")
        choice = int(input('Enter your choice between 1 and 4 : '))
        return choice
