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


def main():
    file = "/home/gyogy/code/advent/inputs/06"
    fish = parse(file)
    for i in range(256):
        print(i)
        fish = pass_day(fish)
        if i == 79:
            print(f"Part 1: {len(fish)} lanternfish after 80 days.")
    print(f"Part 2: {len(fish)} lanternfish after 256 days.")
#    ipdb.set_trace()


if __name__ == "__main__":
    main()

