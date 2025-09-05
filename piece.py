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
    coo     : tuple[int]    : coordinates of the piece                      : (line,column)
    moved   : bool          : True if the piece hasbeen moved previously             
    color   : str           : color of the piece                            : w / b
    type    : str           : type of piece                                 : K / p' / .....
            :   King    -> K
                Queen   -> Q
                Rook    -> r
                Bishop  -> b
                Knight  -> kn
                Pawn    -> p
            :   K for white ; K' for black
    """
    def __init__(self,coo:tuple[int],type:str):
        self.coo = coo
        self.l = coo[0]
        self.c = coo[1]
        self.type = type
        self.moved = False # for rock move
        self.color = ""
        if "'" in self.type: self.color='b'
        else: self.color="w"

