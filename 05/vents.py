import ipdb


def parse(input_file):
    with open(input_file) as inp:
        lines = inp.read().splitlines()
        pairs = [line.split(" -> ") for line in lines]
        points = [int(x) for pair in pairs for half in pair for x in half.split(",")]
        coords = [points[x:x+4] for x in range(0, len(points), 4)]
        return coords


def are_orthogonal(coord):
    return coord[0] == coord[2] or coord[1] == coord[3]


def filter_non_orthogonal(coords):
    return list(filter(lambda x: are_orthogonal(x), coords))


def order(coord):
    x1, y1, x2, y2 = coord
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    return [x1, y1, x2, y2]


def mark_vents(coords):
    dct = {}
    for coord in coords:
        x1, y1, x2, y2 = coord
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if (x, y) not in dct.keys():
                    dct[(x, y)] = 0
                dct[(x, y)] += 1
    return dct

def count_hotspots(dct):
    cnt = 0
    for val in dct.values():
        if val >= 2:
            cnt += 1
    return cnt


def main():
    file = "/home/gyogy/code/advent/inputs/05"
#    file = "/home/gyogy/code/advent/inputs/test"
    all_coords = parse(file)
    ordered_coords = [order(coord) for coord in all_coords]
    coords = filter_non_orthogonal(ordered_coords)
#    ipdb.set_trace()
    log = mark_vents(coords)
    print(f"Part 1: {count_hotspots(log)} orthogonal hotspots.")


if __name__ == "__main__":
    main()

