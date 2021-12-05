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
        boards = [numbers[x:x+25] for x in range(0, len(numbers), 25)]
        return boards


def check(call, board):
    try:
        index = board.index(call)
        board[index] = 0
        return board
    except Value Error:
        return board

def row_has_bingo(board):
    for i in range(0, len(board), 5):
        row = board[i:i+5]
        return sum(row) == 0


def col_has_bingo(board):
    pass


if __name__ == "__main__":
    filename = '/home/gyogy/code/advent/inputs/04'
    calls = get_calls(filename)
    boards = get_boards(filename)
    ipdb.set_trace()
