import logging
import ipdb


logging.basicConfig(filename='log', level=logging.INFO, format='%(levelname)s:%(message)s', filemode='w')


def parse(file):
    with open(file) as f:
        return [[int(octo) for octo in line] for line in f.read().splitlines()]


def cell_in_bounds(matrix, row, col):
    return len(matrix) > row and len(matrix[0]) > col


def cell_is_not_target(row, col, i, j):
    return row != i or col != j


def increment_cells_in(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if (row, col) == (8, 9) or (row, col) == (7, 9):
                          logging.info('%s: %s, %s',
                                       increment_cells_in.__name__, row, col)
            matrix[row][col] += 1


def increment_neighbours_of(matrix, row, col):
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (row, col) == (8, 9) or (row, col) == (7, 9):
                          logging.info('%s: %s, %s', increment_neighbours_of.__name__, row, col)
            if (i, j) == (7, 5):
                ipdb.set_trace()
            if (cell_in_bounds(matrix, i, j)
                    and cell_is_not_target(row, col, i, j)):
                matrix[i][j] += 1


def get_flashes_in(matrix):
    flashes = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] > 9:
                flashes.add((row, col))
    return flashes


def level_flashes(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] > 9:
                matrix[row][col] = 0


def step(matrix):
    increment_cells_in(matrix)
    flashes = get_flashes_in(matrix)

    for f in flashes:
        increment_neighbours_of(matrix, f[0], f[1])
    temp = get_flashes_in(matrix)

    while temp - flashes != set():
        temp -= flashes
        for t in temp:
            flashes.add(t)
            increment_neighbours_of(matrix, t[0], t[1])
        temp = get_flashes_in(matrix)

    level_flashes(matrix)
    for row in matrix:
        print(row)
    print('\n')
    return len(flashes)


def main():
    # test = '11111\n19991\n19191\n19991\n11111'
    # m = [[int(pus) for pus in line] for line in test.splitlines()]
    file = '/home/gyogy/code/advent/inputs/test'
    m = parse(file)
    for row in m:
        print(row)
    part1 = 0
    for i in range(2):
        print(f'Step {i + 1}:')
        part1 += step(m)
    print(f'Part 1: {part1}')


if __name__ == "__main__":
    main()
