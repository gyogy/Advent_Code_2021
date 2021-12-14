import ipdb

OB = '([{<'
CB = ')]}>'

points = {
    None: 0,
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def parse(file):
    with open(file) as f:
        return f.read().splitlines()


def validate(chunk):
    stack = []
    for bracket in chunk:
        try:
            target = OB.index(stack[-1])
        except IndexError:
            target = None

        if bracket in OB:
            stack.append(bracket)
        elif CB.index(bracket) == target:
            stack.pop()
        else:
            return bracket
    return


def part1(data):
    result = 0
    for chunk in data:
        result += points[validate(chunk)]
    return result


if __name__ == '__main__':
    #file = '../inputs/test'
    file = '../inputs/10'
    data = parse(file)
    print(part1(data))

