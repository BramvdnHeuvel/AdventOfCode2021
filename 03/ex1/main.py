

with open('input.txt', 'r') as open_file:
    binaries = [line.strip() for line in open_file]

numbers = len(binaries)
gamma_rate, epsilon_rate = '', ''

for i in range(len(binaries[0])):
    zeros = sum([b[i] == '0' for b in binaries])
    ones  = numbers - zeros

    if zeros < ones:
        gamma_rate   += '1'
        epsilon_rate += '0'
    elif zeros > ones:
        gamma_rate   += '0'
        epsilon_rate += '1'
    else:
        raise ValueError("0 and 1 appear as often.")

print(
    int(gamma_rate, base=2) * int(epsilon_rate, base=2)
)