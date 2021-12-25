import ipdb
from caves import parse, build_graph


class Cave:

    def __init__(self, graph, special=''):
        self.graph = graph
        self.special = special

    @classmethod
    def from_file(cls, file):
        nodes = parse(file)
        graph = build_graph(nodes)
        return cls(graph)

    def is_special(self, neighbour):
        if not hasattr(self.is_special, "count"):
            self.is_special.count = 0

        if neighbour == self.special and self.is_special.count < 2:
            self.is_special.count += 1
            return True
        return False

    def all_lower(neighbours):
        return list(
            filter(
                lambda n:
                (n.islower() and n not in ["start", "end"]), neighbours
            )
        )

    def find_paths(self, frm, to, visited=[], path=[]):
        visited.append(frm)
        path.append(frm)

        if frm == to:
            temp = [x for x in path]
            yield temp
        else:
            for neighbour in self.graph[frm]:
                if neighbour.islower():
                    self.special = neighbour
                    self.count = 0
                    if neighbour not in visited or neighbour.isupper() or self.is_special(neighbour):
                        yield from self.find_paths(self, neighbour, to, visited, path)
                else:
                    for ln in self.all_lower(self.graph[frm]):
                        self.special = ln
                        self.count = 0
                        if neighbour not in visited or neighbour.isupper() or self.is_special(neighbour):
                            yield from self.find_paths(self, neighbour, to, visited, path)

        path.pop()
        visited.pop()


if __name__ == "__main__":
    cave = Cave.from_file('/home/gyogy/code/advent/inputs/test')
    ipdb.set_trace()
    paths = list(cave.find_paths(cave.graph, 'start', 'end'))
    ipdb.set_trace()
