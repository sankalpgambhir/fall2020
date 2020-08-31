
class expr_vector:
    
    __vector    # actual vector for data
    __dim       # dimension of stored data, fixed at init

    def __init__(self, dim = 0, pos = 0, vec = None):

        if vec is None:
            # default constructor
            # check basic conditions
            assert dim > 0          , "Invalid dimension provided!"
            assert pos > 0          , "Invalid position provided!"
            assert dim > pos        , "Position out of dimension range!"

            self.__dim = dim

            self.__vector = [0 for i in range(self.__dim)]
            self.__vector[pos] = 1
        else:
            # copy constructor
            self.__vector = vec
            self.dim = len(self.__vector)
            

    def __add__(self, other):
        # validity of calculus
        assert self.dim == other.dim, "Dimension mismatch!"

        vec = self.__vector + other.__vector

        return 0, 0, vec

    def __sub__(self, other):
        # validity of calculus
        assert self.dim == other.dim, "Dimension mismatch!"

        # multiply other by -1
        vec = [0 for i in range(self.__dim)]
        vec[0] = -1
        minus = expr_vector(0, 0, vec)  # not very efficient, maybe manually invert

        return (self + (minus * other))
    
    def __mul__(self, other):
        # validity of calculus
        assert self.dim == other.dim, "Dimension mismatch!"

        assert const(self) or const(other), "Non-linearity found!"

        vec = None;

        if(const(self)):
            vec = [i * self.__vector[0] for i in other.__vector]
        else:
            vec = [i * other.__vector[0] for i in self.__vector]

        return 0, 0, vec

    def __truediv__(self):
        # validity of calculus
        assert self.dim == other.dim, "Dimension mismatch!"

        assert const(other), "Non-linearity found!"

        vec = other.__vector;
        vec[0] = 1 / vec[0]

        return self * expr_vector(0, 0, vec)


    def __str__(self):
        return str(self.__vector) # make this possibly include var names

    def __len__(self):
        return len(self.__vector)


def const(expv):
    for i in range(1, len(expv)):
        if expv.__vector != 0:
            return False
    
    return True