"""Create tournaments"""


class CreateTournament:

    def __init__(self, view_tournament_creation):
        self.view_tournament_creation = view_tournament_creation

    def new_tournament(self):
        self.view_tournament_creation.prompt_tournament_info()



