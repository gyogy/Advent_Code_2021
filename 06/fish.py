import ipdb


def parse(file):
    with open(file) as f:
        fish = [] 
        for char in f.read().splitlines()[0].split(","):
            fish.append(int(char))
    return fish


def pass_day(fishes):
    next_day = []
    for fish in fishes:
        if fish == 0:
            next_day.append(6)
            next_day.append(8)
        else:
            next_day.append(fish-1)
    return next_day


def copied_solution(init, days):
    state = [init.count(i) for i in range(9)]
    for day in range(days):
        state = state[1:] + state[:1]
        state[6] += state[8]
    return sum(state)

def main():
    file = "/home/gyogy/code/advent/inputs/06"
    fish = parse(file)
    print(copied_solution(fish, 80))
    print(copied_solution(fish, 256))

if __name__ == "__main__":
    main()

