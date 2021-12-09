import ipdb


def parse(file):
    with open(file) as f:
        reads = [[int(x) for x in line] for line in f.read().splitlines()]
        return reads


def in_bounds(matrix, row, col):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return False
    return True


def diagonal(row, col, i, j):
    if row == i or col == j:
        return False
    return True


def neighbours(matrix, row, col):
    return [matrix[i][j] for i in range(row - 1, row + 2) for j in range(col - 1, col + 2) if in_bounds(matrix, i, j) and not diagonal(row, col, i, j)]


def has_lowpoint(neighbours):
    target = neighbours[-3:-2][0]
    if target == min(neighbours):
        return True
    return False


def part1(reads):
    lowpoints = []
    for row in range(len(reads)):
        for col in range(len(reads[0])):
            n = neighbours(reads, row, col)
            if has_lowpoint(n):
                lowpoints.append(n)
    ipdb.set_trace()
    return lowpoints


if __name__ == '__main__':
    file = '../inputs/test'
    reads = parse(file)
    print(part1(reads))

