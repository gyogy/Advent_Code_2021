def parse_input(filename):
    with open(filename, 'r') as f:
        input = f.read()
        return input.splitlines()

def sum_col(array, i):
    return sum([int(bit[i]) for bit in array])

def sum_columns(array):
    sums = []
    for column in zip(*array):
        sums.append(sum([int(bit) for bit in column]))
    return sums

def get_gamma(sums):
    gamma = ''
    for sum in sums:
        if sum > 500:
            gamma += '1'
        else:
            gamma += '0'
    return int(gamma, 2)

def get_epsilon(sums):
    epsilon = ''
    for sum in sums:
        if sum < 500:
            epsilon += '1'
        else:
            epsilon += '0'
    return int(epsilon, 2)

def o_two(array):
    copy = array.copy()

    for i in range(len(copy[0])):
        test = sum_col(copy, i)
        thresh = len(copy)/2

        if test >= thresh:
            copy = list(filter(lambda x: x[i] == '1', copy))
        else:
            copy = list(filter(lambda x: x[i] == '0', copy))

        if len(copy) == 1:
            return int(copy[0], 2)

    return int(copy[0], 2)

def co_two(array):
    copy = array.copy()

    for i in range(len(copy[0])):
        test = sum_col(copy, i)
        thresh = len(copy)/2

        if test >= thresh:
            copy = list(filter(lambda x: x[i] == '0', copy))
        else:
            copy = list(filter(lambda x: x[i] == '1', copy))

        if len(copy) == 1:
            return int(copy[0], 2)

    return int(copy[0], 2)

if __name__ == '__main__':
    readings = parse_input('../inputs/03')
    sums = sum_columns(readings)
    print(f"Part 1: Power consumption is {get_gamma(sums) * get_epsilon(sums)}") 
    print(f"Part 2: Life support rating is {o_two(readings) * co_two(readings)}")

