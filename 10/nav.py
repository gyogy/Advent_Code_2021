import ipdb

OB = '([{<'
CB = ')]}>'

invalid_points = {
    None: 0,
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

incomplete_points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4 
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


def get_incomplete(chunk):
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
            return
    stack.reverse()
    return stack 


def compute(stack):
    result = 0
    for bracket in stack:
        result *= 5
        result +=  incomplete_points[bracket]
    return result


def part1(data):
    result = 0
    for chunk in data:
        result += invalid_points[validate(chunk)]
    return result


def part2(data):
    stacks = [get_incomplete(chunk)
              for chunk in data if get_incomplete(chunk) is not None]
    scores = [compute(stack) for stack in stacks]
    scores.sort()
    middle_score = round(len(scores)/2) - 1
    return scores[middle_score]

if __name__ == '__main__':
    #file = '../inputs/test'
    file = '../inputs/10'
    data = parse(file)
    print(part1(data))
    print(part2(data))

