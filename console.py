
class Console:
    def __init__(self):
        self.type = ''
        self.coo_1 = (0,0)
        self.coo_1 = (0,0)

    def decode(self,cmd:str):
        self.type = self.get_type(cmd)
        self.coo = self.get_coo(cmd.replace(self.type,''))
        self.coo_1 = self.coo[0]
        self.coo_2 = self.coo[1]

    def get_type(self,cmd:str)->str:
        try:
            match len(cmd): #check len of cmd
                case 5:
                    if cmd[0] in ["p","b","r","K","Q"]: # check the piece character
                        type =  cmd[0]
                    else: raise Exception()
                case 6:
                    if cmd[:2] in ["p'","b'","r'","kn","K'","Q'"]:
                        type = cmd[:2]
                    else: raise Exception()
                case 7:
                    if cmd[:3] == "kn'":
                        type = cmd[:3]
                    else: raise Exception()
                case _: raise Exception()
            return(type)
        except Exception:
            print("type or length of cmd incorrect")
            return False
        
    def get_coo(self,cmd:str)->list[tuple]:
        try:
            for e in [0,2]: # set column index from leter to integer for both coordinates 
                match cmd[e]: 
                    case 'a': column_idx = 1
                    case 'b': column_idx = 2
                    case 'c': column_idx = 3
                    case 'd': column_idx = 4
                    case 'e': column_idx = 5
                    case 'f': column_idx = 6
                    case 'g': column_idx = 7
                    case 'h': column_idx = 8
                    case _: raise Exception()
                if e == 0: column_idx_1 = column_idx-1
                if e == 2: column_idx_2 = column_idx-1
            
            for e in [1,3]:
                try:
                    l = int(cmd[e])
                except: raise Exception()
                if l in range(1,9,1):
                    line_idx = l-1
                else: raise Exception()
                if e == 1: line_idx_1 = line_idx
                if e == 3: line_idx_2 = line_idx

        except Exception:
            print("coo of cmd incorrect")
            return False 
        return([(line_idx_1,column_idx_1),(line_idx_2,column_idx_2)])  