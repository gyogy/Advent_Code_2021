def parse_input(filename):
    with open(filename, 'r') as f:
        input = f.read()
        steps = input.splitlines()
        return steps

def part_01(steps):
    fw = [int(step[-1]) for step in steps if step[0] == 'f']
    dn = [int(step[-1]) for step in steps if step[0] == 'd']
    up = [int(step[-1]) for step in steps if step[0] == 'u']
    return sum(fw) * (sum(dn) - sum(up))

def part_02(steps):
    x = 0; aim = 0; depth = 0;

    for step in steps:
        dir = step[0]
        magn = int(step[-1])

        if dir == 'f':
            x += magn
            depth += aim * magn
        if dir == 'd':
            aim += magn
        if dir == 'u':
            aim -= magn
    return x * depth

def main(filename):
    steps = parse_input(filename)
    print(f'Part 1: Final position is {part_01(steps)}.')
    print(f'Part 2: Final position is {part_02(steps)}.')

if __name__ == "__main__":
    main('/home/gyogy/code/advent/inputs/02')
