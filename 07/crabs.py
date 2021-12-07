import ipdb


def parse(file):
    with open(file) as f:
        return [int(x) for x in f.read().splitlines()[0].split(",")]


def calc_fuel(pos):
    unique = set(pos)
    costs = []
    for u in unique:
        fuel = 0
        for p in pos:
            fuel += abs(u - p)
        costs.append(fuel)
    return min(costs)


def calc_fuel_2(pos):
    cost = float('inf')
    fuel = 0

    for i in range(min(pos), max(pos) + 1):
        fuel = 0
        for p in pos:
            fuel += sum(range(1, abs(i-p) + 1))
        cost = min(cost, fuel)

    return cost


def main():
    file = "/home/gyogy/code/advent/inputs/07"
    pos = parse(file)
    print(f"Part 1: Smallest fuel cost is {calc_fuel(pos)}.")
    print(f"Part 2: Smallest fuel cost is {calc_fuel_2(pos)}.")


if __name__ == "__main__":
    main()

