from board import Board
from console import Console
from rules import Rules
from piece import *

##########################
# init and show board
##########################
board = Board()
board.show()

##########################
# start
##########################
game_ongoing = True
player = "white"
consol = Console()
while game_ongoing:
    not_decoded = True
    print(f"{player} to play :")

##########################
# get and decode input cmd
##########################
    while not_decoded:
        cmd = input()
        try:
            consol.decode(cmd)
            not_decoded = False
        except:pass

##########################
# check move
##########################
    rules = Rules()
    piece = Piece(consol.coo_1,consol.type)
    print(rules.diff_start_end_coo(consol.coo_1,consol.coo_2))
    print(rules.check_piece_exist(piece,board))
    print(rules.check_destination_color(piece,board,consol.coo_2))