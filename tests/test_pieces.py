from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import *

class TestQueen:
    @staticmethod
    def test_queens_moves():
        complete_moves = [Square.at(5, 5),Square.at(3, 3),Square.at(5, 3),Square.at(3, 5),Square.at(7, 7),Square.at(4, 7),Square.at(7, 4)]
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(4, 4)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        for move in complete_moves:
            # Assert
            assert move in moves

    @staticmethod
    def test_queens_moves_with_obstruction():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(4, 4)
        board.set_piece(square, queen)

        obstructing_square = Square.at(2, 2)
        obstruction = Rook(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        obstructing_square2 = Square.at(4, 2)
        obstruction2 = Rook(Player.WHITE)
        board.set_piece(obstructing_square2, obstruction2)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves
        assert obstructing_square2 not in moves

    @staticmethod
    def test_queens_boundary_moves():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(4, 4)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(8, 8) not in moves
        assert Square.at(8, 4) not in moves

    @staticmethod
    def test_queens_can_capture():

        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(4, 4)
        board.set_piece(square, queen)

        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(2, 2)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.BLACK)
        enemy2_square = Square.at(5, 4)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

class TestBishops:
    @staticmethod
    def test_bishops_moves():
        complete_moves = [Square.at(5, 5),Square.at(3, 3),Square.at(5, 3),Square.at(3, 5),Square.at(7, 7)]
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        square = Square.at(4, 4)
        board.set_piece(square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        for move in complete_moves:
            # Assert
            assert move in moves

    @staticmethod
    def test_bishops_moves_with_obstruction():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        square = Square.at(4, 4)
        board.set_piece(square, bishop)

        obstructing_square = Square.at(2, 2)
        obstruction = Rook(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_bishops_boundary_moves():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        square = Square.at(4, 4)
        board.set_piece(square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(8, 8) not in moves

    @staticmethod
    def test_bishops_can_capture():

        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        square = Square.at(4, 4)
        board.set_piece(square, bishop)

        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(2, 2)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.BLACK)
        enemy2_square = Square.at(5, 5)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

class TestKnights:

    @staticmethod
    def test_knights_moves():
        complete_moves = [Square.at(2, 2),Square.at(4, 2),Square.at(5, 3),Square.at(5, 5),Square.at(4, 6),Square.at(2, 6),Square.at(1, 5),Square.at(1, 3)]
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(3, 4)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        for move in complete_moves:
            # Assert
            assert move in moves

    @staticmethod
    def test_knights_moves_with_obstruction():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(3, 4)
        board.set_piece(square, knight)

        obstructing_square = Square.at(2, 2)
        obstruction = Rook(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_knights_boundary_moves():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(3, 6)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(2, 8) not in moves

    @staticmethod
    def test_knights_can_capture():

        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        knight_square = Square.at(3, 4)
        board.set_piece(knight_square, knight)

        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(2, 2)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.BLACK)
        enemy2_square = Square.at(5, 5)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves


class TestRooks:

    @staticmethod
    def test_rooks_can_move_up_multiple_squares():
        complete_moves = [Square.at(4, 4),Square.at(5, 4),Square.at(6, 4),Square.at(7, 4)]
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        square = Square.at(3, 4)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        for move in complete_moves:
            # Assert
            assert move in moves

    @staticmethod
    def test_rooks_can_move_down_multiple_squares():
        complete_moves = [Square.at(2, 4),Square.at(1, 4),Square.at(0, 4)]
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        square = Square.at(3, 4)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        for move in complete_moves:
            # Assert
            assert move in moves

    @staticmethod
    def test_rooks_can_move_left_multiple_squares():
        complete_moves = [Square.at(3, 3),Square.at(3, 2),Square.at(3, 1),Square.at(3, 0)]
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        square = Square.at(3, 4)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        for move in complete_moves:
            # Assert
            assert move in moves

    @staticmethod
    def test_rooks_can_move_right_multiple_squares():
        complete_moves = [Square.at(3, 5),Square.at(3, 6),Square.at(3, 7)]
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        square = Square.at(3, 4)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        for move in complete_moves:
            # Assert
            assert move in moves

    @staticmethod
    def test_rook_cannot_move_up_if_piece_in_front():
        moves_list = [Square.at(5, 4),Square.at(6, 4),Square.at(7, 4)]
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(4, 4)
        board.set_piece(rook_square, rook)

        obstructing_square = Square.at(5, 4)
        obstruction = Rook(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        for move in moves_list:
            # Assert
            assert move not in moves

    @staticmethod
    def test_rook_cannot_move_down_if_piece_in_front():
        moves_list = [Square.at(3, 4),Square.at(2, 4),Square.at(1, 4),Square.at(0, 4)]
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(4, 4)
        board.set_piece(rook_square, rook)

        obstructing_square = Square.at(3, 4)
        obstruction = Rook(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        for move in moves_list:
            # Assert
            assert move not in moves

    @staticmethod
    def test_rook_cannot_move_left_if_piece_in_front():
        moves_list = [Square.at(4, 3),Square.at(4, 2),Square.at(4, 1),Square.at(4, 0)]
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(4, 4)
        board.set_piece(rook_square, rook)

        obstructing_square = Square.at(4, 3)
        obstruction = Rook(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        for move in moves_list:
            # Assert
            assert move not in moves

    @staticmethod
    def test_rook_cannot_move_right_if_piece_in_front():
        moves_list = [Square.at(4, 5),Square.at(4, 6),Square.at(4, 7)]
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(4, 4)
        board.set_piece(rook_square, rook)

        obstructing_square = Square.at(4, 5)
        obstruction = Rook(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        for move in moves_list:
            # Assert
            assert move not in moves

    @staticmethod
    def test_rooks_cannot_move_out_of_bounds():
        moves_list = [Square.at(-1, 4),Square.at(8, 4),Square.at(4, 8),Square.at(4, -1)]
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        square = Square.at(4, 4)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        for move in moves_list:
            # Assert
            assert move not in moves

    @staticmethod
    def test_rooks_can_capture_horizontally():

        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(3, 4)
        board.set_piece(rook_square, rook)

        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(3, 5)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.BLACK)
        enemy2_square = Square.at(3, 3)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves
        assert Square.at(3,6) not in moves
        assert Square.at(3,2) not in moves

    @staticmethod
    def test_rooks_can_capture_vertically():

        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(3, 4)
        board.set_piece(rook_square, rook)

        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(4, 4)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.BLACK)
        enemy2_square = Square.at(2, 4)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves
        assert Square.at(5,4) not in moves
        assert Square.at(1,4) not in moves

class TestPawns:

    @staticmethod
    def test_white_pawns_can_move_up_one_square():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(2, 4) in moves

    @staticmethod
    def test_black_pawns_can_move_down_one_square():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) in moves

    @staticmethod
    def test_white_pawn_can_move_up_two_squares_if_not_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) in moves

    @staticmethod
    def test_black_pawn_can_move_down_two_squares_if_not_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves

    @staticmethod
    def test_white_pawn_cannot_move_up_two_squares_if_already_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        starting_square = Square.at(1, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(2, 4)
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_black_pawn_cannot_move_down_two_squares_if_already_moved():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        starting_square = Square.at(6, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(5, 4)
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) not in moves

    @staticmethod
    def test_white_pawn_cannot_move_if_piece_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(5, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_pawn_cannot_move_if_piece_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(3, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_pawn_cannot_move_two_squares_if_piece_two_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(6, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_black_pawn_cannot_move_two_squares_if_piece_two_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(2, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_white_pawn_cannot_move_two_squares_if_piece_one_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(1, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(2, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) not in moves

    @staticmethod
    def test_black_pawn_cannot_move_two_squares_if_piece_one_in_front():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(6, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(5, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_white_pawn_cannot_move_at_top_of_board():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(7, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_pawn_cannot_move_at_bottom_of_board():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(0, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_pawns_can_capture_diagonally():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(4, 5)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.BLACK)
        enemy2_square = Square.at(4, 3)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

    @staticmethod
    def test_black_pawns_can_capture_diagonally():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        enemy1 = Pawn(Player.WHITE)
        enemy1_square = Square.at(2, 5)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.WHITE)
        enemy2_square = Square.at(2, 3)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

    @staticmethod
    def test_white_pawns_cannot_move_diagonally_except_to_capture():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        friendly = Pawn(Player.WHITE)
        friendly_square = Square.at(4, 5)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 3) not in moves
        assert Square.at(4, 5) not in moves

    @staticmethod
    def test_black_pawns_cannot_move_diagonally_except_to_capture():

        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        friendly = Pawn(Player.BLACK)
        friendly_square = Square.at(2, 5)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) not in moves
        assert Square.at(2, 5) not in moves
