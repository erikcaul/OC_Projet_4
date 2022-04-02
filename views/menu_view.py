"""Menu view"""


class MenuView:
    """Main menu"""

    def prompt_menu_choice(self):
        """Prompt for a choice"""
        print("Choose an option : \n"
              "1. Create a tournament\n"
              "2. Create a player\n"
              "3. Add a player to a tournament\n"
              "4. create a round for a tournament\n"
              "5. Play a round\n"
              "6. Update players ranking\n"
              "7. Reports\n"
              "8. Save data\n"
              # "9. Load data saved\n"
              "9. Quit\n")
        choice = input('Enter your choice between 1 and 9 : \n')
        return choice
