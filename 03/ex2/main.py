with open('input.txt', 'r') as open_file:
    binaries = [line.strip() for line in open_file]

numbers = len(binaries)
oxygen_nums, co2_nums = binaries, binaries

for i in range(len(binaries[0])):
    ox_zeros = sum([b[i] == '0' for b in oxygen_nums])
    ox_ones  = len(oxygen_nums) - ox_zeros
    
    co_zeros = sum([b[i] == '0' for b in co2_nums])
    co_ones  = len(co2_nums) - co_zeros

    if len(oxygen_nums) > 1:
        if ox_zeros <= ox_ones:
            oxygen_nums = [o for o in oxygen_nums if o[i] == '1']
        else:
            oxygen_nums = [o for o in oxygen_nums if o[i] == '0']
    
    if len(co2_nums) > 1:
        if co_zeros <= co_ones:
            co2_nums = [o for o in co2_nums if o[i] == '0']
        else:
            co2_nums = [o for o in co2_nums if o[i] == '1']

print(oxygen_nums)
print(co2_nums)

print(
    int(oxygen_nums[0], base=2) * 
    int(co2_nums[0], base=2)
)