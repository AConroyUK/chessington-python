"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

def inBounds(num):
    return num >= 0 and num <= 7

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        moves = []
        multiplier = -1
        start_row = 6

        current_square = board.find_piece(self)
        if self.player == Player.WHITE:
            multiplier = 1
            start_row = 1

        #vertical moves
        if inBounds(current_square.row+(1*multiplier)):
            if board.get_piece(Square.at(current_square.row+(1*multiplier),current_square.col)) == None:
                moves.append(Square.at(current_square.row+(1*multiplier),current_square.col))
                if current_square.row == start_row and \
                board.get_piece(Square.at(current_square.row+(2*multiplier),current_square.col)) == None:
                    moves.append(Square.at(row=current_square.row+(2*multiplier),col=current_square.col))

        #diagonal moves
        if inBounds(current_square.row+(1*multiplier)):
            for horizontal in [-1,1]:
                if inBounds(current_square.col+(1*horizontal)):
                    piece = board.get_piece(Square.at(current_square.row+(1*multiplier),current_square.col+(1*horizontal)))
                    if piece != None:
                        if piece.player != self.player:
                            moves.append(Square.at(current_square.row+(1*multiplier),current_square.col+(1*horizontal)))

        return moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        moves = []
        list = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
        current_square = board.find_piece(self)
        for vertical,horizontal in list:
            if inBounds(current_square.row+vertical) and inBounds(current_square.col+horizontal):
                square = Square.at(current_square.row+vertical,current_square.col+horizontal)
                piece = board.get_piece(square)
                if piece == None:
                    moves.append(square)
                elif piece.player != self.player:
                    moves.append(square)

        return moves


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        moves = []
        current_square = board.find_piece(self)
        for vertical,horizontal in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            for i in range(1,8):
                if inBounds(current_square.row+(vertical*i)) and inBounds(current_square.col+(horizontal*i)):
                     square = Square.at(current_square.row+(vertical*i),current_square.col+(horizontal*i))
                     piece = board.get_piece(square)
                     if piece == None:
                         moves.append(square)
                     elif piece.player != self.player:
                         moves.append(square)
                         break
                     else:
                         break

        return moves


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        moves = []

        current_square = board.find_piece(self)

        for direction in [1,-1]:
            if direction == 1: max = 8
            else: max = -1

            for vertical in range(current_square.row+direction,max,direction):
                square = Square.at(vertical,current_square.col)
                piece = board.get_piece(square)
                if piece == None:
                    moves.append(square)
                elif piece.player != self.player:
                    moves.append(square)
                    break
                else:
                    break
            for horizontal in range(current_square.col+direction,max,direction):
                square = Square.at(current_square.row,horizontal)
                piece = board.get_piece(square)
                if piece == None:
                    moves.append(square)
                elif piece.player != self.player:
                    moves.append(square)
                    break
                else:
                    break

        return moves


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        moves = []

        current_square = board.find_piece(self)

        for vertical,horizontal in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            for i in range(1,8):
                if inBounds(current_square.row+(vertical*i)) and inBounds(current_square.col+(horizontal*i)):
                     square = Square.at(current_square.row+(vertical*i),current_square.col+(horizontal*i))
                     piece = board.get_piece(square)
                     if piece == None:
                         moves.append(square)
                     elif piece.player != self.player:
                         moves.append(square)
                         break
                     else:
                         break

        for direction in [1,-1]:
            if direction == 1: max = 8
            else: max = -1

            for vertical in range(current_square.row+direction,max,direction):
                square = Square.at(vertical,current_square.col)
                piece = board.get_piece(square)
                if piece == None:
                    moves.append(square)
                elif piece.player != self.player:
                    moves.append(square)
                    break
                else:
                    break
            for horizontal in range(current_square.col+direction,max,direction):
                square = Square.at(current_square.row,horizontal)
                piece = board.get_piece(square)
                if piece == None:
                    moves.append(square)
                elif piece.player != self.player:
                    moves.append(square)
                    break
                else:
                    break

        return moves


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []
