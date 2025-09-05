from board import *
from piece import *

class Rules:
    """
    Rules of Chess Game
    -------------------------------------------------------------------
    linear_moves    : list[tuple]       : possible moves for linear move    :  [(diff_x,diff_y),....]
    diag_moves      : list[tuple]       : possible moves for diag move      :  [(diff_x,diff_y),....]
    get_l_moves     : list[tuple]       : possible moves for knight         :  [(diff_x,diff_y),....]
    
    """
    def __init__(self):
        self.linear_moves = self.get_linear_moves()
        self.diag_moves = self.get_diag_moves()
        self.l_move = self.get_l_moves()

    def check_rules(self,piece:Piece,destination:tuple,board:Board)->bool:
        if self.diff_start_end_coo(piece.coo,destination) and self.check_piece_exist(piece,board) and self.check_destination_color(piece,board,destination):
            print("ok")

    def get_diag_moves(self)->list[tuple]:
        moves = []
        for i in range(-7,8,1):
            moves.append((i,i))
        del moves[moves.index((0,0))]
        return moves

    def get_linear_moves(self)->list[tuple]:
        moves = []
        for i in range(-7,8,1):
            moves.append((0,i))
            moves.append((i,0))
        del moves[moves.index((0,0))]
        return moves

    def get_l_moves(self)->list[tuple]: # move of knight
        moves = []
        for x in [-2,-1,1,2]:
            for y in [-2,-1,1,2]:
                if abs(x) != abs(y): moves.append((x,y))
    
    def diff_start_end_coo(self,coo_1:tuple,coo_2:tuple)->bool: # check if start piece is not going to it's own position
        if coo_1 != coo_2: return True
        else: 
            print("the piece can't go to it's own position")
            return False
    
    def check_piece_exist(self,piece:Piece,board:Board)->bool: # check if the piece exist
        piece_in_board = board.tab[piece.l][piece.c]
        if piece_in_board != False:
            if piece_in_board == piece:
                return True
            else: 
                print("no piece at this position")
                return False
        else: 
            print("no piece at this position")
            return False

    def check_destination_color(self,piece:Piece,board:Board,coo_2:tuple)->bool: # check if white try to eat a white piece
        destination = board.tab[coo_2[0]][coo_2[1]]
        if destination != None:
            if destination.color == piece.color:
                print("the piece can't take a piece with the same color")
                return False
            else: return True
        else: return True

