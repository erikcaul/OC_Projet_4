"""Reports management"""
from views.report_view import ReportView
from controllers.menu_controller import MainLoop
from controllers.player_controller import PlayerController
from views.tournament_view import TournamentView
from controllers.tournament_controller import TournamentController

class ReportManagement:
    def __init__(self, active=True):
        self.report_view = ReportView()
        self.main_loop = MainLoop()
        self.active = active
        self.player_controller = PlayerController()
        self.tournament_view = TournamentView()
        self.tournament_controller = TournamentController()


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
        all_players = self.player_controller.players
        sorted_all_players = sorted(all_players, key=lambda p: p.name, reverse=True) # le mettre dans Tools ? sorted_by_element "name" or "ranking"
        self.report_view.print_element_report(sorted_all_players)

    def print_all_players_list_by_ranking(self):
        all_players = self.player_controller.players
        sorted_all_players = sorted(all_players, key=lambda p: p.ranking, reverse=True)
        self.report_view.print_element_report(sorted_all_players)

    def print_tournament_players_list_by_alpha_order(self):
        pick_tournament = self.tournament_view.pick_up_tournament
        tournament_players = pick_tournament.players
        sorted_tournament_players = sorted(tournament_players, key=lambda p: p.name, reverse=True)
        self.report_view.print_element_report(sorted_tournament_players)

    def print_tournament_players_list_by_ranking(self):
        pick_tournament = self.tournament_view.pick_up_tournament
        tournament_players = pick_tournament.players
        sorted_tournament_players = sorted(tournament_players, key=lambda p: p.ranking, reverse=True)
        self.report_view.print_element_report(sorted_tournament_players)

    def print_all_tournaments_list(self):
        all_tournament = self.tournament_controller.tournaments_list
        sorted_all_tournament = sorted(all_tournament, key=lambda p: p.name, reverse=True)
        self.report_view.print_element_report(sorted_all_tournament)

    def print_all_rounds_tournament_list(self):
        pass

    def print_all_games_tournament_list(self):
        pass

