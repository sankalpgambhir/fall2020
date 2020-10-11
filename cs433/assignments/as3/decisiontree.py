import z3
import decision

class decision_tree:
    def __init__(self, size, l = None, r = None):

        assert (l == None) or (isinstance(l, decision_tree)), "Invalid data type passed for l!" 
        assert (r == None) or (isinstance(r, decision_tree)), "Invalid data type passed for r!"
        assert (isinstance(size, int)) and (size > 0), "Invalid decision size!" 

        self.left = l
        self.right = r

        pass