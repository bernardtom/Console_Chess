from piece import Piece

class Board:
    def __init__(self):
        pieces_init_pos= [Piece((1,0),"p"),Piece((1,1),"p"),Piece((1,2),"p"),Piece((1,3),"p"),Piece((1,4),"p"),Piece((1,5),"p"),Piece((1,6),"p"),Piece((1,7),"p"),
                         Piece((6,0),"p'"),Piece((6,1),"p'"),Piece((6,2),"p'"),Piece((6,3),"p'"),Piece((6,4),"p'"),Piece((6,5),"p'"),Piece((6,6),"p'"),Piece((6,7),"p'"),
                         Piece((0,0),"r"),Piece((0,7),"r"),Piece((7,0),"r'"),Piece((7,7),"r'"),
                         Piece((0,1),"kn"),Piece((0,6),"kn"),Piece((7,1),"kn'"),Piece((7,6),"kn'"),
                         Piece((0,2),"b"),Piece((0,5),"b"),Piece((7,2),"b'"),Piece((7,5),"b'"),
                         Piece((0,3),"Q"),Piece((7,3),"Q'"),
                         Piece((0,4),"K"),Piece((7,4),"K'")]
        self.tab = self.fill_board(pieces_init_pos)

    def fill_board(self,pieces:list[Piece])->list:
        board = []
        for l in range(8):
            line_tab = []
            for c in range(8):
                for p in pieces:
                    if p.coo == (l,c):
                        line_tab.append(p)
                        break
                    else: 
                        if p == pieces[-1]:
                            line_tab.append(None)
                            break
            board.append(line_tab)
        return board
    
    def show(self):
        print("\n\r")
        i=0
        for l in reversed(self.tab): # reverse the line because we print from top to bottom but first line should be at the bottom
            column_idx = [8,7,6,5,4,3,2,1]
            print(f"{column_idx[i]}  ",end='')
            print("#  ",end='')
            i+=1
            for c in l:
                if c == None: print("  .  ",end='')
                else: 
                    match len(c.type):
                        case 1: str = f"  {c.type}  "
                        case 2: str = f" {c.type}  "
                        case 3: str = f" {c.type} "
                    print(str,end='')
            print('\r')
            print("   #")

        print("    # # # # # # # # # # # # # # # # # # # # # ")
        print("     ","  A  "," B  "," C  "," D  "," E  "," F  "," G  "," H  ")