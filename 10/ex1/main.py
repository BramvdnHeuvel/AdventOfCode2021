class Stack:
    def __init__(self):
        self.values = []
    
    def add(self, value):
        self.values.append(value)
    
    def pop(self):
        self.values, outcast = self.values[:-1], self.values[-1]
        return outcast

DIGITS = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>'
}
SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

with open('input.txt', 'r') as open_file:
    syntaxes = [line.strip() for line in open_file]

score = 0

for line in syntaxes:
    s = Stack()

    for char in line:
        if char in DIGITS.keys():
            s.add(char)
        else:
            open_tag = s.pop()
            if DIGITS[open_tag] != char:
                score += SCORES[char]
                break

print(score)
