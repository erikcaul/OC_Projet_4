"""Reports management"""
from views.report_view import ReportView
from controllers.menu_controller import MainLoop

class ReportManagement:
    def __init__(self, active=True):
        self.report_view = ReportView()
        self.main_loop = MainLoop()
        self.active = active

    def choose_a_report(self):
        """Run the reports options"""
        menu = {
            "1": self.print_all_players_list_by_alpha_order,
            "2": self.print_all_players_list_by_ranking,
            "3": self.print_tournament_players_list_by_alpha_order,
            "4": self.print_tournament_players_list_by_ranking,
            "5": self.print_all_tournaments_list,
            "6": self.print_all_rounds_tournament_list,
            "7": self.print_all_games_tournament_list, 
            "8": self.main_loop.run
        }

        while self.active:
            choice = self.report_view.prompt_report_choice
            if choice in menu:
                menu[choice]()
            else:
                print("invalid option")

    def print_all_players_list_by_alpha_order(self):
        pass

    def print_all_players_list_by_ranking(self):
        pass

    def print_tournament_players_list_by_alpha_order(self):
        pass

    def print_tournament_players_list_by_ranking(self):
        pass

    def print_all_tournaments_list(self):
        pass

    def print_all_rounds_tournament_list(self):
        pass

    def print_all_games_tournament_list(self):
        pass

