import json
from math import prod

with open('input.txt', 'r') as open_file:
    values = ''.join(line.strip() for line in open_file)
    message = ''.join([bin(int(m, 16))[2:].zfill(4) for m in values])

class Packet:
    def __init__(self, message):
        self.packet = {
            'version' : int(message[0:3], 2),
            'type'    : int(message[3:6], 2)
        }
        self.length = 0
        self.children = []

        if self.packet['type'] == 4:
            i = 6
            while message[i] != '0':
                i += 5
            
            content = message[6:i+5]

            self.length          = 6 + len(content)
            self.packet['value'] = self.parse_literal_value(content)
        
        # Operator package
        else:
            length_type = message[6]

            # Number of bits in sub-packets
            if length_type == '0':
                bit_length = int(message[7:22], 2)
                self.length = 22 + bit_length

                current_length = 0
                while current_length < bit_length:
                    self.children.append(
                        Packet(message[22+current_length:])
                    )
                    current_length += self.children[-1].length

            # Number of sub-packets
            else:
                packet_amount = int(message[7:18], 2)
                self.length = 18

                for _ in range(packet_amount):
                    self.children.append(
                        Packet(message[self.length:])
                    )
                    self.length += self.children[-1].length

    def to_json(self):
        return {
            'packet': self.packet,
            'length': self.length,
            'children': [
                c.to_json() for c in self.children
            ]
        }

    def version_sums(self):
        return self.packet['version'] + sum(
            [p.version_sums() for p in self.children]
        )
    
    def calculate(self):
        lower_values = [c.calculate() for c in self.children]

        type_numbers = {
            0 : sum,
            1 : prod,
            2 : min,
            3 : max,
            5 : lambda cs : int(cs[0] > cs[1]),
            6 : lambda cs : int(cs[0] < cs[1]),
            7 : lambda cs : int(cs[0] == cs[1])
        }

        if self.packet['type'] == 4:
            return self.packet['value']
        else:
            return type_numbers[self.packet['type']](lower_values)

    @staticmethod
    def parse_literal_value(content):
        binary_string, i = '', 1

        while (i+4 <= len(content)):
            binary_string += content[i:i+4]
            if content[i-1] == '0':
                break
            i += 5
        
        return int(binary_string, 2)

packet = Packet(message)
print(
    json.dumps(
        packet.to_json()
    )
)
print(packet.version_sums())
print(packet.calculate())