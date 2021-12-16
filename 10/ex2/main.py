import statistics

class Stack:
    def __init__(self):
        self.values = []
    
    def add(self, value):
        self.values.append(value)
    
    def pop(self):
        self.values, outcast = self.values[:-1], self.values[-1]
        return outcast
    
    def empty_all(self):
        l = reversed(self.values)
        self.values = []
        return l

DIGITS = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>'
}
SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

with open('input.txt', 'r') as open_file:
    syntaxes = [line.strip() for line in open_file]

scores = []

for line in syntaxes:
    s = Stack()

    for char in line:
        if char in DIGITS.keys():
            s.add(char)
        else:
            open_tag = s.pop()
            if DIGITS[open_tag] != char:
                break
    else:
        # The line is not corrupted!
        score = 0

        for char in s.empty_all():
            score *= 5
            score += SCORES[DIGITS[char]]

        scores.append(score)

print(scores)
print(statistics.median(scores))
