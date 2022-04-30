"""Reports management"""
from views.report_view import ReportView
from views.tournament_view import TournamentView


class ReportManagement:
    def __init__(self, player_controller, tournament_controller, active=True):
        self.report_view = ReportView()
        # self.main_loop = MainLoop()
        # self.active = active
        self.player_controller = player_controller
        self.tournament_view = TournamentView()
        self.tournament_controller = tournament_controller
        self.tournaments_list = self.tournament_controller.tournaments_list

    def choose_a_report(self):
        """Run the reports options"""
        self.active = True
        menu = {
            "1": self.print_all_players_list_by_alpha_order,
            "2": self.print_all_players_list_by_ranking,
            "3": self.print_tournament_players_list_by_alpha_order,
            "4": self.print_tournament_players_list_by_ranking,
            "5": self.print_all_tournaments_list,
            "6": self.print_all_rounds_tournament_list,
            "7": self.print_all_games_tournament_list,
            "8": self.stop_report
        }

        while self.active:
            choice = self.report_view.prompt_report_choice()
            if choice in menu:
                menu[choice]()
            else:
                print("invalid option")

    def stop_report(self):
        self.active = False

    def print_all_players_list_by_alpha_order(self):
        print("All players list by alphabetical order : ")
        all_players = self.player_controller.players
        sorted_all_players = sorted(all_players, key=lambda p: p.name)
        self.report_view.print_players_report(sorted_all_players)

    def print_all_players_list_by_ranking(self):
        print("All players list by ranking : ")
        all_players = self.player_controller.players
        sorted_all_players = sorted(all_players,
                                    key=lambda p: p.ranking, reverse=True)
        self.report_view.print_players_report(sorted_all_players)

    def print_tournament_players_list_by_alpha_order(self):
        pick_tournament = self.tournament_view.pick_up_tournament(
                                               self.tournaments_list
                                               )
        tournament_players = pick_tournament.players
        sorted_tournament_players = sorted(tournament_players,
                                           key=lambda p: p.name
                                           )
        print("Tournament players list by alphabetical order : ")
        self.report_view.print_players_report(sorted_tournament_players)

    def print_tournament_players_list_by_ranking(self):
        pick_tournament = self.tournament_view.pick_up_tournament(
                                               self.tournaments_list
                                               )
        tournament_players = pick_tournament.players
        sorted_tournament_players = sorted(tournament_players,
                                           key=lambda p: p.ranking,
                                           reverse=True
                                           )
        print("Tournament players list by ranking : ")
        self.report_view.print_players_report(sorted_tournament_players)

    def print_all_tournaments_list(self):
        sorted_all_tournament = sorted(self.tournaments_list,
                                       key=lambda p: p.name
                                       )
        print("List of all the tournaments : ")
        self.report_view.print_tournament_report(sorted_all_tournament)

    def print_all_rounds_tournament_list(self):
        pick_tournament = self.tournament_view.pick_up_tournament(
                                               self.tournaments_list
                                               )
        print("Tournament rounds list : ")
        self.report_view.print_rounds_report(pick_tournament.rounds)

    def print_all_games_tournament_list(self):
        pick_tournament = self.tournament_view.pick_up_tournament(
                                               self.tournaments_list
                                               )
        print("Tournament games list : ")
        for round in pick_tournament.rounds:
            print(round.round_name)
            self.report_view.print_games_report(round.games)
