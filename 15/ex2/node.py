class Node:
    def __init__(self, coords, score):
        self.coords = coords
        self.score  = score

        self.relative_score = score
        self.parent = None
    
    def add_parent(self, other):
        self.relative_score += other.relative_score
        self.parent = other
    
    def __lt__(self, other):
        return self.relative_score < other.relative_score
    
    def trace(self):
        trace, cursor = [], self
        while cursor is not None:
            trace.append(cursor.coords)
            cursor = cursor.parent
        return trace