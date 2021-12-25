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


def pt2(graph, node, visited):
    res = []
    new_visit = visited + [node]

    if node == 'end':
        ipdb.set_trace()
        return [new_visit]

    for n in graph[node]:
        if n != 'start':
            if n.isupper():
                temp_res = pt2(graph, n, new_visit)
#                ipdb.set_trace()
                res.extend(temp_res)
            else:
                lcase = [i for i in new_visit if i.islower()]
                twice = any([True for i in lcase if lcase.count(i) >1])
                if (twice and new_visit.count(n) < 1) or (not twice and new_visit.count(n) < 2):
                    temp_res = pt2(graph, n, new_visit)
                    res.extend(temp_res)
    return res


if __name__ == '__main__':
    file = '/home/gyogy/code/advent/inputs/test'
    graph = build_graph(parse(file))
    print(f"Part 2: {len(pt2(graph, 'start', []))}")
