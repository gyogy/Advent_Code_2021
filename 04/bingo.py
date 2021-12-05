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
    wins= []
    winners = []

    for call in calls:
        for i, brd in enumerate(brds):
            if i in wins:
                pass
            else:
                for row in brd:
                    if call in row:
                        row.remove(call)
                    if len(row) == 0:
                        s = sum([x for rw in brd for x in rw])
                        wins.append(i)
                        winners.append({'board': i, 'call': call, 'sum': s, 'product': call * s})
                        if len(winners) == 100:
                            ipdb.set_trace()
                        break 
    return winners


if __name__ == "__main__":
    filename = '/home/gyogy/code/advent/inputs/04'
    calls = get_calls(filename)
    boards = get_boards(filename)
    t_boards = transpose(boards)
    winners = bingo(t_boards, calls)
    ipdb.set_trace()

