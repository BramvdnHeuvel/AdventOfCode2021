from typing import List, Tuple, Dict

with open('input.txt') as open_file:
    instructions = [tuple(line.strip().split(' ')) for line in open_file]

class Program:
    def __init__(self, instructions : List[Tuple[str, str, str]]) -> None:
        self.instructions = instructions
    
    def run_program(self, number : int) -> int:
        v = {'x' : 0, 'y': 0, 'z': 0, 'w': 0}
        n, ni = str(number), 0

        for i in self.instructions:
            if ni >= len(n):
                self.run_instruction(i, v, float('inf'), ni)
            else:
                ni = self.run_instruction(i, v, int(n[ni]), ni)
        
        return v
    
    def run_instruction(self,
            instruction : Tuple[str, str, str], 
            variables : Dict[str, int],
            input_number : int,
            input_index : int) -> None:
        programs = {
            'add' : lambda a, b : a+b,
            'mul' : lambda a, b : a*b,
            'div' : lambda a, b : a // b if a/b > 0 else -a // b,
            'mod' : lambda a, b : a % b,
            'eql' : lambda a, b : int(a == b)
        }

        # inp instruction
        if instruction[0] == 'inp':
            if input_number == float('inf'):
                raise ValueError("Input cannot be infinite.")
            variables[instruction[1]] = input_number
            return input_index + 1
        
        # Other instructions
        num_1 = variables[instruction[1]]
        num_2 = int(instruction[2]) if instruction[2] not in variables else variables[instruction[2]]

        variables[instruction[1]] = programs[instruction[0]](num_1, num_2)
        return input_index

p = Program(instructions)
# i = int('1' + ''.join(['0' for _ in range(14)]))
i = 11111111111111

if __name__ == '__main__':
    while i > 0:
        i += 1

        if '0' in str(i):
            continue
        
        zero_value = p.run_program(i)['z']
        # print(f"{i}\t-->\t{zero_value}")


        if i % 10000 == 9999:
            print(f"{i}\t-->\t{zero_value}")

        if zero_value == 0:
            print(f"{i}\t-->\t{zero_value}")
            break