class ScoreQueue:
    def __init__(self):
        self.values = []
    
    def put(self, value):
        self.values.append(value)
    
    def get(self):
        try:
            out, self.values = self.values[0], self.values[1:]
        except IndexError:
            return None
        else:
            return out
    