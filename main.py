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
rules = Rules()
while game_ongoing:
    not_decoded = True
    print(f"{player} to play :")

########################## get and decode input cmd ##########################
    while not_decoded:
        cmd = input()
        try:
            consol.decode(cmd)
            not_decoded = False
        except:pass

########################## check move ##########################  
    piece = Piece(consol.coo_1,consol.type)
    if rules.check_rules(piece,consol.coo_2,board):
        pass