"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

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
        if current_square.row+(1*multiplier) >= 0 and current_square.row+(1*multiplier) <= 7 :
            if board.get_piece(Square.at(current_square.row+(1*multiplier),current_square.col)) == None:
                moves.append(Square.at(current_square.row+(1*multiplier),current_square.col))
                if current_square.row == start_row and \
                board.get_piece(Square.at(current_square.row+(2*multiplier),current_square.col)) == None:
                    moves.append(Square.at(row=current_square.row+(2*multiplier),col=current_square.col))

        #diagonal moves
        if current_square.row+(1*multiplier) >= 0 and current_square.row+(1*multiplier) <= 7 :
            for horizontal in [-1,1]:
                if current_square.col+(1*horizontal) >= 0 and current_square.col+(1*horizontal) <= 7:
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
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []
