class Game:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None

    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.winner:
            self.board[row][col] = self.current_player
            self.check_winner()
            if not self.winner:
                self.switch_player()
            return True
        return False
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        b = self.board

        # Check rows & columns
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != "":
                self.winner = b[i][0]
                return
            if b[0][i] == b[1][i] == b[2][i] != "":
                self.winner = b[0][i]
                return

        # Check diagonals
        if b[0][0] == b[1][1] == b[2][2] != "":
            self.winner = b[0][0]
        elif b[0][2] == b[1][1] == b[2][0] != "":
            self.winner = b[0][2]
    def is_draw(self):
        if self.winner:
            return False
        return all(cell != "" for row in self.board for cell in row)

    def reset(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winner = None