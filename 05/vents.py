def parse(input_file):
    with open(input_file) as inp:
        lines = inp.read().splitlines()
        pairs = [line.split(" -> ") for line in lines]
        points = [int(x) for pair in pairs for half in pair for x in half.split(",")]
        coords = [points[x:x+4] for x in range(0, len(points), 4)]
        return coords


def is_orthogonal(coord):
    return coord[0] == coord[2] or coord[1] == coord[3]


def filter_non_orthogonal(coords):
    return list(filter(lambda x: is_orthogonal(x), coords))


def order(coord):
    x1, y1, x2, y2 = coord
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1
        return [x1, y1, x2, y2]
    if y1 > y2:
        x1, y1, x2, y2 = x2, y2, x1, y1
        return [x1, y1, x2, y2]

    return [x1, y1, x2, y2]


def mark_line(coord, dct):
    x1, y1, x2, y2 = coord
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if (x, y) not in dct.keys():
                dct[(x, y)] = 0
            dct[(x, y)] += 1
    return dct


def mark_diagonal(coord, dct):
    x1, y1, x2, y2 = coord
    increase_x = x2 - x1 > 0
    increase_y = y2 - y1 > 0

    for i in range(abs(x1 - x2) + 1):
        if (x1, y1) not in dct.keys():
            dct[(x1, y1)] = 0
        dct[(x1, y1)] += 1

        if increase_x:
            x1 += 1
        else:
            x1 -= 1
        if increase_y:
            y1 += 1
        else:
            y1 -= 1
    return dct


def mark_vents(coords):
    dct = {}
    for coord in coords:
        if is_orthogonal(coord):
            dct = mark_line(coord, dct)
        else:
            dct = mark_diagonal(coord, dct)
    return dct


def count_hotspots(dct):
    cnt = 0
    for val in dct.values():
        if val >= 2:
            cnt += 1
    return cnt


def main():
    file = "/home/gyogy/code/advent/inputs/05"
    all_coords = parse(file)
    ordered_coords = [order(coord) for coord in all_coords]
    filtered_coords = filter_non_orthogonal(ordered_coords)
    part1 = mark_vents(filtered_coords)
    part2 = mark_vents(ordered_coords)
    print(f"Part 1: {count_hotspots(part1)} orthogonal hotspots.")
    print(f"Part 2: {count_hotspots(part2)} orthogonal hotspots.")


if __name__ == "__main__":
    main()

