class EqualMixin:
    """
    Used only for comparason between 2 objects of Piece class
    """
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

class Piece(EqualMixin):
    """
    Chess Piece
    -------------------------------------------------------------------
    coo     : coordinates of the piece  : tuple[int]    : (line,column)
    moved   : True if the piece has     : bool
              been moved previously 
    color   : color of the piece        : str           : w / b
    type    : type of piece             : str           : K / p' / .....
            :   King    -> K
                Queen   -> Q
                Rook    -> r
                Bishop  -> b
                Knight  -> kn
                Pawn    -> p
            : K for white ; K' for black
    """
    def __init__(self,coo:tuple[int],type:str):
        self.coo = coo
        self.type = type
        self.moved = False # for rock move
        self.color = ""
        if "'" in self.type: self.color='b'
        else: self.color="w"

