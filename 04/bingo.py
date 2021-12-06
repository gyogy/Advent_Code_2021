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


def transpose(board):
    cols = []
    for i in range(5):
        col = []
        for j in range(5):
            col.append(board[j][i])
        cols.append(col)
    return cols 


def sum_remaining(board):
    return sum([x for row in board for x in row])


def mark(call, board):
    for row in board:
        if call in row:
            hit = row.index(call)
            row[hit] = 0
            if sum(row) == 0:
                break


def bingo(board):
    return [0, 0, 0, 0, 0] in board


def check_rows(call, board):
#    ipdb.set_trace()
    if bingo(board):
        remainder = sum_remaining(board)
        print("BINGO!")
        print(f"    {call} * {remainder} = {call * remainder}")

def check_cols(call, board):
    tboard = transpose(board)
    if bingo(tboard):
        check_rows(call, tboard)
        board.append([0, 0, 0, 0, 0])



def main():
    file = '/home/gyogy/code/advent/inputs/04'
    calls = get_calls(file)
    boards = get_boards(file)
    for call in calls:
        for board in boards:
            if not bingo(board): 
                mark(call, board)
                check_rows(call, board)
                check_cols(call, board)


if __name__ == "__main__":
    main()

