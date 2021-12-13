import ipdb


def parse(file):
    with open(file) as f:
        reads = [[int(x) for x in line] for line in f.read().splitlines()]
        return reads


def is_in_bounds(matrix, row, col):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
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


def get_ortho_indeces(matrix, row, col):
    return [(i, j)
            for i in range(row - 1, row + 2)
            for j in range(col - 1, col + 2)
            if is_in_bounds(matrix, i, j)
            and not is_target(row, col, i, j)
            and not is_diagonal(row, col, i, j)]

def bfs(matrix, cell, visited=None, queue=None):
    if visited == None:
        visited = []

    if queue == None:
        queue = []
 
    visited.append(cell)
    queue.append(cell)

    while queue:
        new = queue.pop(0)
        for neigh in get_ortho_indeces(matrix,new[0],new[1]):
            if reads[neigh[0]][neigh[1]] == 9:
               continue 
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)
    return len(visited)

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

def part2(reads):
    lowpoints = []
    basins = []
    for row in range(len(reads)):
        for col in range(len(reads[0])):
            target = reads[row][col]
            n = get_orthogonal_neighbours(reads, row, col)
            if is_lowpoint(target, n):
                lowpoints.append((row, col))
    for lp in lowpoints:
        basins.append(bfs(reads, lp))
    basins.sort()
    return basins[-1] * basins[-2] * basins [-3]

if __name__ == '__main__':
    #file = '../inputs/test'
    file = '../inputs/09'
    reads = parse(file)
    #ipdb.set_trace()
    print(part1(reads))
    print(part2(reads))

