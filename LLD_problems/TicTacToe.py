from enum import Enum

class PieceType(Enum):
    X = 'X'
    O = 'O'

class PlayingPiece:
    def __init__(self, piece_type):
        self.piece_type = piece_type
    
    def get_type(self):
        return self.piece_type
    
class Piece_X(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.X)

class Piece_O(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O)

class Player:
    def __init__(self, name, playing_piece) -> None:
        self.name = name
        self.playing_piece = playing_piece

class Board:
    def __init__(self, size) -> None:
        self.size = size
        self.board = [[None for _ in range(self.size)] for _ in range(size)]

    def display_board(self):
        display_row = ''
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col]:
                    display_row += self.board[row][col] + '  ' + '|' 
                else:
                    display_row += '    ' + '  ' + '|' 
            display_row += '\n'
        print(display_row)

    def place_piece(self, r, c, piece):
        if 0 <= r < self.size and 0 <= c < self.size:
            if self.board[r][c] is None:
                self.board[r][c] = piece
                return True
            else:
                return False
        else:
            return "Enter Valid row and col"








"""player1 = Player('player1', Piece_X())
player2 = Player('player2', Piece_O())
print(player1.playing_piece.get_type())"""

board = Board(3)
board.display_board()