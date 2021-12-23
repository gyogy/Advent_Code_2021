import ipdb


def parse(file):
    with open(file) as f:
        return [
            node
            for line in f.read().splitlines()
            for node in line.split('-')
        ]


def build_graph(nodes):
    a = nodes[0:-1:2]
    b = nodes[1::2]
    graph = {}
    for pair in zip(a, b):
        if pair[0] in graph.keys():
            graph[pair[0]].append(pair[1])
        else:
            graph.update({pair[0]: [pair[1]]})
        if pair[1] in graph.keys():
            graph[pair[1]].append(pair[0])
        else:
            graph.update({pair[1]: [pair[0]]})
    return graph


def find_pt1_paths(graph, frm, to, visited=[], path=[]):
    visited.append(frm)
    path.append(frm)

    if frm == to:
        temp = [x for x in path]
        yield temp
    else:
        for neighbour in graph[frm]:
            if neighbour not in visited or neighbour.isupper():
                yield from find_pt1_paths(graph, neighbour, to, visited, path)
    path.pop()
    visited.pop()


def main():
    file = '/home/gyogy/code/advent/inputs/test'
    nodes = parse(file)
    graph = build_graph(nodes)
    pt1_paths = list(find_pt1_paths(graph, 'start', 'end'))
    print(f'Part1: {len(pt1_paths)}')
#    ipdb.set_trace()


if __name__ == '__main__':
    main()
