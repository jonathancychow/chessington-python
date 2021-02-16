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
        current_square = board.find_piece(self)
        colour = self.player
        moves = []
        if colour == Player.WHITE:
            if current_square.row == 1:
                if board.get_piece(Square.at(current_square.row+1,current_square.col)) is None:
                    moves.append(Square.at(current_square.row+1,current_square.col))
                if (board.get_piece(Square.at(current_square.row+1,current_square.col)) is None) and (board.get_piece(Square.at(current_square.row+2,current_square.col)) is None):
                    moves.append(Square.at(current_square.row+2,current_square.col))
            else:
                if current_square.row+1 <= 7:
                    if board.get_piece(Square.at(current_square.row+1,current_square.col)) is None:
                        moves.append(Square.at(current_square.row+1,current_square.col))
                    if current_square.col+1 <= 7:
                        if board.get_piece(Square.at(current_square.row+1,current_square.col+1)) is not None:
                            if (board.get_piece(Square.at(current_square.row+1,current_square.col+1)).player == Player.BLACK):
                                moves.append(Square.at(current_square.row+1,current_square.col+1))
                    if current_square.col-1 >= 0:
                        if board.get_piece(Square.at(current_square.row+1,current_square.col-1)) is not None:
                            if (board.get_piece(Square.at(current_square.row+1,current_square.col-1)).player == Player.BLACK):
                                moves.append(Square.at(current_square.row+1,current_square.col-1))

        elif colour == Player.BLACK:
            if current_square.row == 6:
                if board.get_piece(Square.at(current_square.row-1,current_square.col)) is None:
                    moves.append(Square.at(current_square.row-1,current_square.col))
                if (board.get_piece(Square.at(current_square.row-1,current_square.col)) is None) and (board.get_piece(Square.at(current_square.row-2,current_square.col)) is None):
                    moves.append(Square.at(current_square.row-2,current_square.col))
            else:
                if current_square.row-1 >= 0:
                    if board.get_piece(Square.at(current_square.row-1,current_square.col)) is None:
                        moves.append(Square.at(current_square.row-1,current_square.col))
                    if current_square.col+1 <= 7:
                        if board.get_piece(Square.at(current_square.row-1,current_square.col+1)) is not None:
                            if (board.get_piece(Square.at(current_square.row-1,current_square.col+1)).player == Player.WHITE):
                                moves.append(Square.at(current_square.row-1,current_square.col+1))
                    if current_square.col-1 >= 0:
                        if board.get_piece(Square.at(current_square.row-1,current_square.col-1)) is not None:
                            if (board.get_piece(Square.at(current_square.row-1,current_square.col-1)).player == Player.WHITE):
                                moves.append(Square.at(current_square.row-1,current_square.col-1))

        return moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        colour = self.player
        moves = []
        #above
        if current_square.row+2 <= 7:
            if (board.get_piece(Square.at(current_square.row+1,current_square.col)) is None) and (board.get_piece(Square.at(current_square.row+2,current_square.col)) is None):
                # up and right
                if current_square.col+1 <= 7:
                    if board.get_piece(Square.at(current_square.row+2,current_square.col+1)) is None:
                        moves.append(Square.at(current_square.row+2,current_square.col+1))
                    elif (board.get_piece(Square.at(current_square.row+2,current_square.col+1)).player != colour):
                        moves.append(Square.at(current_square.row+2,current_square.col+1))
                # up and left
                if current_square.col-1 >= 0:
                    if board.get_piece(Square.at(current_square.row+2,current_square.col-1)) is None:
                        moves.append(Square.at(current_square.row+2,current_square.col-1))
                    elif (board.get_piece(Square.at(current_square.row+2,current_square.col-1)).player != colour):
                        moves.append(Square.at(current_square.row+2,current_square.col-1))

        #down
        if current_square.row-2 >= 0:
            if (board.get_piece(Square.at(current_square.row-1,current_square.col)) is None) and (board.get_piece(Square.at(current_square.row-2,current_square.col)) is None):
                # up and right
                if current_square.col+1 <= 7:
                    if board.get_piece(Square.at(current_square.row-2,current_square.col+1)) is None:
                        moves.append(Square.at(current_square.row-2,current_square.col+1))
                    elif (board.get_piece(Square.at(current_square.row-2,current_square.col+1)).player != colour):
                        moves.append(Square.at(current_square.row-2,current_square.col+1))
                # up and left
                if current_square.col-1 >= 0:
                    if board.get_piece(Square.at(current_square.row-2,current_square.col-1)) is None:
                        moves.append(Square.at(current_square.row-2,current_square.col-1))
                    elif (board.get_piece(Square.at(current_square.row-2,current_square.col-1)).player != colour):
                        moves.append(Square.at(current_square.row-2,current_square.col-1))
   
        #right
        if current_square.col+2 <= 7:
            if (board.get_piece(Square.at(current_square.row,current_square.col+2)) is None) and (board.get_piece(Square.at(current_square.row,current_square.col+1)) is None):
                
                if current_square.row+1 <= 7:
                    if board.get_piece(Square.at(current_square.row+1,current_square.col+2)) is None:
                        moves.append(Square.at(current_square.row+1,current_square.col+2))
                    elif (board.get_piece(Square.at(current_square.row+1,current_square.col+2)).player != colour):
                        moves.append(Square.at(current_square.row+1,current_square.col+2))
                
                if current_square.row-1 >= 0:
                    if board.get_piece(Square.at(current_square.row-1,current_square.col+2)) is None:
                        moves.append(Square.at(current_square.row-1,current_square.col+2))
                    elif (board.get_piece(Square.at(current_square.row-1,current_square.col+2)).player != colour):
                        moves.append(Square.at(current_square.row-1,current_square.col+2))

        #left
        if current_square.col-2 >= 0:
            if (board.get_piece(Square.at(current_square.row,current_square.col-2)) is None) and (board.get_piece(Square.at(current_square.row,current_square.col-1)) is None):
                
                if current_square.row+1 <= 7:
                    if board.get_piece(Square.at(current_square.row+1,current_square.col-2)) is None:
                        moves.append(Square.at(current_square.row+1,current_square.col-2))
                    elif (board.get_piece(Square.at(current_square.row+1,current_square.col-2)).player != colour):
                        moves.append(Square.at(current_square.row+1,current_square.col-2))
                
                if current_square.row-1 >= 0:
                    if board.get_piece(Square.at(current_square.row-1,current_square.col-2)) is None:
                        moves.append(Square.at(current_square.row-1,current_square.col-2))
                    elif (board.get_piece(Square.at(current_square.row-1,current_square.col-2)).player != colour):
                        moves.append(Square.at(current_square.row-1,current_square.col-2))
   

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
        current_square = board.find_piece(self)
        colour = self.player
        moves = []

        #above
        if current_square.row+1 <= 7:
            if board.get_piece(Square.at(current_square.row+1,current_square.col)) is None:
                moves.append(Square.at(current_square.row+1,current_square.col))
            elif (board.get_piece(Square.at(current_square.row+1,current_square.col)).player != colour):
                    moves.append(Square.at(current_square.row+1,current_square.col))
            if current_square.col+1 <= 7:
                if board.get_piece(Square.at(current_square.row+1,current_square.col+1)) is None:
                    moves.append(Square.at(current_square.row+1,current_square.col+1))
                elif (board.get_piece(Square.at(current_square.row+1,current_square.col+1)).player != colour):
                    moves.append(Square.at(current_square.row+1,current_square.col+1))
            if current_square.col-1 >= 0:
                if board.get_piece(Square.at(current_square.row+1,current_square.col-1)) is None:
                    moves.append(Square.at(current_square.row+1,current_square.col-1))
                elif (board.get_piece(Square.at(current_square.row+1,current_square.col-1)).player != colour):
                    moves.append(Square.at(current_square.row+1,current_square.col-1))
        #side
        if current_square.col+1 <= 7:
            if board.get_piece(Square.at(current_square.row,current_square.col+1)) is None:
                moves.append(Square.at(current_square.row,current_square.col+1))
            elif (board.get_piece(Square.at(current_square.row,current_square.col+1)).player != colour):
                moves.append(Square.at(current_square.row,current_square.col+1))
        if current_square.col-1 >= 0:
            if board.get_piece(Square.at(current_square.row,current_square.col-1)) is None:
                moves.append(Square.at(current_square.row,current_square.col-1))
            elif (board.get_piece(Square.at(current_square.row,current_square.col-1)).player != colour):
                moves.append(Square.at(current_square.row,current_square.col-1))

        #below
        if current_square.row-1 <= 7:
            if board.get_piece(Square.at(current_square.row-1,current_square.col)) is None:
                moves.append(Square.at(current_square.row-1,current_square.col))
            elif (board.get_piece(Square.at(current_square.row-1,current_square.col)).player != colour):
                    moves.append(Square.at(current_square.row-1,current_square.col))
            if current_square.col-1 <= 7:
                if board.get_piece(Square.at(current_square.row-1,current_square.col+1)) is None:
                    moves.append(Square.at(current_square.row-1,current_square.col+1))
                elif (board.get_piece(Square.at(current_square.row-1,current_square.col+1)).player != colour):
                    moves.append(Square.at(current_square.row-1,current_square.col+1))
            if current_square.col-1 >= 0:
                if board.get_piece(Square.at(current_square.row-1,current_square.col-1)) is None:
                    moves.append(Square.at(current_square.row-1,current_square.col-1))
                elif (board.get_piece(Square.at(current_square.row-1,current_square.col-1)).player != colour):
                    moves.append(Square.at(current_square.row-1,current_square.col-1))

        return moves