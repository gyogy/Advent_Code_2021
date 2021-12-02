def parse_input(filename):
    with open(filename, 'r') as f:
        input = f.read()
        steps = input.splitlines()
        return steps

def part_01(steps):
    fw = [step[-1] for step in steps if step[0] == 'f']
    dn = [step[-1] for step in steps if step[0] == 'd']
    up = [step[-1] for step in steps if step[0] == 'u']
    return sum(fw) * (sum(dn) - sum(up))

def part_02():
    for step in steps:
        if step[0] == 'f':
            x += int(step[-1])
            depth += aim * int(step[-1])
        if step[0] == 'd':
            aim += int(step[-1])
        if step[0] == 'u':
            aim -= int(step[-1])

if __name__ == "__main__":
    print(__file__)
