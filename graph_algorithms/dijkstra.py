# Dijkstra's Algorithm
from heapq import heappush, heappop


class Vertex(object):
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def __repr__(self):
        return self.id


class Graph(object):
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        return self.vert_dict.get(n)

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()


def dijkstra(graph, start, end):
    # for each vertices, we use this to keep track of the parent
    parent = {}
    # keep track of distance from the start
    distance_from_start = {}
    # uses a priority queue. we can implement this later
    priority_heap = []
    # initialize the distance from start and parent nodes
    for vertex_id in graph.get_vertices():
        vertex = graph.get_vertex(vertex_id)
        if vertex != start:
            parent[vertex] = None
            distance_from_start[vertex] = float("inf")  # set distance to infinity
            heappush(priority_heap, (distance_from_start[vertex], vertex))

    distance_from_start[start] = 0  # set the start point as 0
    heappush(priority_heap, (distance_from_start[start], start))

    while priority_heap:
        _, u = heappop(priority_heap)  # returns the node with lowest priority
        for v, v_weight in u.adjacent.iteritems():
            # distance from start + distance from originating node to u
            alt = distance_from_start[u] + v.get_weight(u)
            if alt < distance_from_start[v]:
                distance_from_start[v] = alt
                parent[v] = u

    # return parent and distance from start
    return distance_from_start, parent


if __name__ == "__main__":
    g = Graph()
    start = g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    end = g.add_vertex('f')

    g.add_edge('a', 'b', 2)
    g.add_edge('a', 'e', 4)
    g.add_edge('a', 'c', 1)
    g.add_edge('e', 'c', 4)
    g.add_edge('b', 'e', 1)
    g.add_edge('b', 'd', 3)
    g.add_edge('c', 'd', 2)
    g.add_edge('c', 'f', 4)
    g.add_edge('d', 'f', 1)

    # print g.vert_dict

    """
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))
    """

    distance_from_start, parent = dijkstra(g, start, end)
    print distance_from_start
    print parent

