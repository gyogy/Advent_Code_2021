import ipdb


def parse(file):
    with open(file) as f:
        reads = [[int(x) for x in line] for line in f.read().splitlines()]
        return reads


def is_in_bounds(matrix, row, col):
    if (row < 0 or row >= len(matrix)
    or col < 0 or col >= len(matrix[0])):
        return False
    return True


def is_diagonal(row, col, i, j):
    if row == i or col == j:
        return False
    return True


def is_target(row, col, i, j):
    if row != i or col != j:
        return False 
    return True


def get_all_neighbours(matrix, row, col):
    return [matrix[i][j]
            for i in range(row - 1, row + 2)
            for j in range(col - 1, col + 2)
            if is_in_bounds(matrix, i, j)
            and not is_target(row, col, i, j)]


def get_orthogonal_neighbours(matrix, row, col):
    return [matrix[i][j]
            for i in range(row - 1, row + 2)
            for j in range(col - 1, col + 2)
            if is_in_bounds(matrix, i, j)
            and not is_diagonal(row, col, i, j)
            and not is_target(row, col, i, j)]


def is_lowpoint(target, neighbours):
    if target > min(neighbours) or target in neighbours:
        return False
    return True 


def part1(reads):
    lowpoints = []
    for row in range(len(reads)):
        for col in range(len(reads[0])):
            target = reads[row][col]
            n = get_orthogonal_neighbours(reads, row, col)
            if is_lowpoint(target, n):
                lowpoints.append(target + 1)
    return sum(lowpoints)


if __name__ == '__main__':
    #file = '../inputs/test'
    file = '../inputs/09'
    reads = parse(file)
    #ipdb.set_trace()
    print(part1(reads))

