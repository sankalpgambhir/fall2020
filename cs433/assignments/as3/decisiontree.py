import z3
import decision

num_colors = 0 # no colors by default
set_size = 0

class color_pos:
    def __init__(self, color, not_holds = None):
        assert (not_holds is None) or (isinstance(not_holds, list)), "Invalid data type passed for not_holds!"
        assert all((isinstance(c, int) and c <= num_colors and c >= 0) for c in not_holds), "Invalid color in not_holds!"

        assert (isinstance(color, int) and color <= num_colors and color >= 0), "Invalid color value"

        self.color = color
        
        if not_holds is not None:
            self.not_holds = not_holds
        else:
            self.not_holds = []

        pass

class decision_tree:
    def __init__(self, col = None, child = None):

        assert (child is None) or (isinstance(child, list)), "Invalid data type passed for children!" 
        assert child is not [], "Empty children list!"
        assert all(isinstance(d, decision_tree) for d in child), "Invalid tree node in children!"

        if child is None:
            self.children = []
        else:
            self.children = child

        if col is not None:
            assert set_size == len(col), "Color list and size mismatch!"
            assert all(isinstance(c, color_pos) for c in col), "Invalid type passed for color pos!"
            self.colors = col
        else:
            self.colors = [0 for i in range(set_size)]
        
        self.condition = None # True/False = SAT/UNSAT once set

        pass

    def check_condition(self):
        return decision.check_sat(self.colors) and all(d.check_condition() for d in self.children)

    def branch(self):
        assert self.condition is not False, "UNSAT parent branching!"

        new_colors = decision.make_decision(self.colors)

        if new_colors is None:
            return False

        self.children.append(decision_tree(len(self.colors), new_colors))
        
        return True