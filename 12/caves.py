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


def is_special(neighbour, special):
    if not hasattr(is_special, "count"):
        is_special.count = 0

    if neighbour == special and is_special.count < 2:
        is_special.count += 1
        return True
    return False


def all_lower(neighbours):
    return list(
        filter(
            lambda n: (n.islower() and n not in ["start", "end"]), neighbours
        )
    )


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


def find_pt2_paths(graph, frm, to, special='', visited=[], path=[]):
    visited.append(frm)
    path.append(frm)

    if frm == to:
        temp = [x for x in path]
        yield temp

    for n in graph[frm]:
        if n != 'start':
            if n.isupper():


    path.pop()
    visited.pop()

def visit2(p, node, visited):
  # recursively find paths - and add 'em to res (resulting list)
  res = []
  # next visited node
  new_visit = visited + [node]
  if node == 'end':
    return [new_visit]
  for n in p[node]:
    if n != 'start':
      # uppercase nodes can be visited any time
      if n.isupper():
        temp_res = visit2(p, n, new_visit)
        res.extend(temp_res)
      else:
        # any lowercase node - just one can be visited twice
        l_case = [i for i in new_visit if i.islower()]
        twice = any([True for i in l_case if l_case.count(i) > 1])
        if (twice and new_visit.count(n) < 1) or (not twice and new_visit.count(n) < 2):
          temp_res = visit2(p, n, new_visit)
          res.extend(temp_res)
  return res


def main():
    file = '/home/gyogy/code/advent/inputs/test'
    nodes = parse(file)
    graph = build_graph(nodes)
    pt1_paths = list(find_pt1_paths(graph, 'start', 'end'))
    pt2_paths = list(find_pt2_paths(graph, 'start', 'end'))
    print(f'Part1: {len(pt1_paths)}')
    print(f'Part2: {len(pt2_paths)}')
    for p in pt2_paths:
        print(p)
#    ipdb.set_trace()


if __name__ == '__main__':
#    main()
    file = '/home/gyogy/code/advent/inputs/test'
    nodes = parse(file)
    graph = build_graph(nodes)
    paths = visit2(graph, 'start', [])
    ipdb.set_trace()
