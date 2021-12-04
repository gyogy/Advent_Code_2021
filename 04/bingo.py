import ipdb
from copy import deepcopy

def get_calls(filename):
    with open(filename, 'r') as f:
        raw = f.read().splitlines()[0]
        return [int(x) for x in raw.split(",")]


def get_boards(filename):
    with open(filename, 'r') as f:
        raw = f.read().splitlines()[2:]
        numbers = [int(x) for r in raw for x in r.split(' ')  if x != '']
        rows = [numbers[x:x+5] for x in range(0, len(numbers), 5)]
        boards = [rows[x:x+5] for x in range(0, len(rows), 5)]
        return boards


def transpose(boards):
    t_boards = []
    for board in boards:
        cols = []
        for i in range(5):
            col = []
            for j in range(5):
                col.append(board[j][i])
            cols.append(col)
        t_boards.append(cols)
    return t_boards


def bingo(boards, calls):
    brds = deepcopy(boards)
    clls = deepcopy(calls)

    for i, num in enumerate(clls):
        for j, brd in enumerate(brds):
            for row in brd:
                if num in row:
                    row.remove(num)
                if len(row) == 0:
                    print(f"Winning call is {i}: {num}.")
                    print(f"Winning board is {j}.")
                    print(f"Sum of remaining numbes on the winning board is: {sum([x for rw in brd for x in rw])}")
                    print(f"Call X Board = {num * sum([x for rw in brd for x in rw])}")
                    return


if __name__ == "__main__":
    filename = '/home/gyogy/code/advent/inputs/04'
    calls = get_calls(filename)
    boards = get_boards(filename)
    t_boards = transpose(boards)
    bingo(boards, calls)
    ipdb.set_trace()

