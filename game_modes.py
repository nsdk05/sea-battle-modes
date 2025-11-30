import random
from game_logic import GameBoard

class Game:
    def __init__(self):
        self.board1=GameBoard()
        self.board2=GameBoard()
        self.current_player=1
        self.game_over=False
        self.winner=None

    def switch_player(self):
        if self.current_player==1:
            self.current_player=2
        else:
            self.current_player=1

    def make_shot(self,x,y):
        if self.game_over:
            return "game_over"
        if self.current_player==1:
            target_board=self.board2
        else:
            target_board=self.board1
        result=target_board.shoot(x,y)
        if result=="win":
            self.game_over=True
            self.winner=self.current_player
        if result=="miss":
            self.switch_player()
        return result
class Game:
    def __init__(self):
        self.board1=GameBoard()
        self.board2=GameBoard()
        self.current_player=1
        self.game_over=False
        self.winner=None

    def switch_player(self):
        if self.current_player==1:
            self.current_player=2
        else:
            self.current_player=1

    def make_shot(self,x,y):
        if self.game_over:
            return "game_over"
        if self.current_player==1:
            target_board=self.board2
        else:
            target_board=self.board1
        result=target_board.shoot(x,y)
        if result=="win":
            self.game_over=True
            self.winner=self.current_player
        if result=="miss":
            self.switch_player()
        return result

class TwoPlayerGame(Game):
    def __init__(self):
        super().__init__()
        self.phase="setup1"

    def setup_phase_complete(self,player):
        if player==1 and self.phase=="setup1":
            self.phase="setup2"
            return True
        elif player==2 and self.phase=="setup2":
            self.phase="play"
            return True
        return False

    def get_current_phase(self):
        return self.phase
