from board import Board
from console import Console

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
    
    print(consol.coo_1,consol.coo_2,consol.type)
