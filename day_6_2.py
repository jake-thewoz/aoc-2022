import data_getter

data = data_getter.get_data(6)

def four_are_different(index):
    bits = data[index:(index+14)]
    for bit in bits:
        if bits.count(bit) > 1:
            return False
    print(bits)
    return index + 14

for i in range(len(data)-15):
    if four_are_different(i) != False:
        print(f'The last bit of the start packet is at index (+1) {four_are_different(i)}.')
        break
