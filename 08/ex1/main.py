import re

with open('input.txt', 'r') as open_file:
    digits = [line for line in open_file]

def find_unique_digits(display):
    output_values = display.strip().split('|')[1]
    return len([part for part in output_values.split(' ') if len(part) in [2, 3, 4, 7]])

print(sum(
    [find_unique_digits(d) for d in digits]
))