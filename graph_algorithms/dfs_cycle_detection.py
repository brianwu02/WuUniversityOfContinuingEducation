# Graph
class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, vertex):
        if vertex.name not in self.neighbors:
            self.neighbors.append(vertex)


class Graph(object):
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        return False

    def add_directed_edge(self, u, v):
        """
        :type u: str key value for node u
        :type v: str key value for node v
        """
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(self.get_vertex(v))

    def add_undirected_edge(self, u, v):
        self.add_directed_edge(u, v)
        self.add_directed_edge(v, u)

    def number_of_vertices(self):
        return len(self.vertices)

    def get_vertex(self, n):
        """
        :type n: str
        return the Vertex
        """
        return self.vertices[n]

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))

    def __iter__(self):
        return iter(self.vertices.values())


def is_path_cyclic(node, visited):
    """
    @type G: Graph
    @param G: our Graph

    @type node: Vertex
    @param node: the vertex we are currently visiting

    @type visited: set
    @param visited: set of visited paths

    @rtype: bool
    @return: if a path is cyclic
    """
    stack = [node]
    while stack:
        u = stack.pop()
        if u in visited:
            return True
        visited.add(u)
        for v in u.neighbors:
            stack.append(v)
    return False


def is_graph_cyclic(graph):
    """
    @type graph: Graph
    @param graph: graph for which we run a dfs-variant cycle check algorithm

    @rtype: boolean
    @return: whether the graph is cyclic
    """
    # keep track of keys that have been visted
    visited = set()
    # our stack
    for node in graph:
        if node not in visited:
            if is_path_cyclic(node, visited):
                return True
    return False


def is_cyclic(G):
    """
    returns True if directed graph g has a cycle.
    """
    path = set()
    visited = set()

    def visit(vertex):
        # if the vertex has been visited, return False
        if vertex in visited:
            return False
        visited.add(vertex)
        path.add(vertex)
        for neighbor in vertex.neighbors:
            if neighbor in path or visit(neighbor):
                return True
        path.remove(vertex)
        return False

    graph_is_cyclic = any(visit(v) for v in G)
    return graph_is_cyclic


def cyclic_graph_example_c():
    """
    create a disconnected graph
    A -> B -> C
    E -> F -> G -> G
    """
    g = Graph()
    # create the vertices
    g.add_vertex(Vertex('a'))
    g.add_vertex(Vertex('b'))
    g.add_vertex(Vertex('c'))
    g.add_vertex(Vertex('d'))
    g.add_vertex(Vertex('e'))
    g.add_vertex(Vertex('f'))
    g.add_vertex(Vertex('g'))
    # add the directed edges for subgraph 1
    g.add_directed_edge('a', 'b')
    g.add_directed_edge('b', 'c')
    # add the directed edges for subgraph 2
    g.add_directed_edge('e', 'f')
    g.add_directed_edge('f', 'g')
    g.add_directed_edge('g', 'h')
    g.add_directed_edge('g', 'g')
    
    # stack-based dfs variant
    assert is_graph_cyclic(g)
    # recursive-based dfs variant
    assert is_cyclic(g)

def cyclic_graph_example_a():
    """
    g1 is a cyclic graph a -> b -> c -> a
    """
    # create the graph
    g1 = Graph()
    # create the vertices
    g1.add_vertex(Vertex('a'))
    g1.add_vertex(Vertex('b'))
    g1.add_vertex(Vertex('c'))
    # add the directed edges
    g1.add_directed_edge('a', 'b')
    g1.add_directed_edge('b', 'c')
    g1.add_directed_edge('c', 'a')
    # check
    assert is_graph_cyclic(g1)
    assert is_cyclic(g1)


def cyclic_graph_example_b():
    """
    g is a cyclic graph a -> b -> c -> c
    """
    g = Graph()
    g.add_vertex(Vertex('a'))
    g.add_vertex(Vertex('b'))
    g.add_vertex(Vertex('c'))
    # add the directed edges
    g.add_directed_edge('a', 'b')
    g.add_directed_edge('b', 'c')
    g.add_directed_edge('c', 'c')

    assert is_graph_cyclic(g)
    assert is_cyclic(g)


def acyclic_graph_example_a():
    """
    a -> b -> c

    this graph is not acyclic
    """
    g = Graph()
    g.add_vertex(Vertex('a'))
    g.add_vertex(Vertex('b'))
    g.add_vertex(Vertex('c'))
    # add the directed edges
    g.add_directed_edge('a', 'b')
    g.add_directed_edge('b', 'c')

    assert not is_cyclic(g)
    assert not is_graph_cyclic(g)


def acyclic_graph_example_b():
    """
    a -> b -> c
    d -> e -> f
    """
    g = Graph()
    # add subpath 1
    g.add_vertex(Vertex('a'))
    g.add_vertex(Vertex('b'))
    g.add_vertex(Vertex('c'))
    # add subpath 2
    g.add_vertex(Vertex('d'))
    g.add_vertex(Vertex('e'))
    g.add_vertex(Vertex('f'))
    # add the directed edges
    g.add_directed_edge('a', 'b')
    g.add_directed_edge('b', 'c')
    g.add_directed_edge('d', 'e')
    g.add_directed_edge('e', 'f')

    assert not is_cyclic(g)
    assert not is_graph_cyclic(g)


if __name__ == "__main__":
    cyclic_graph_example_a()
    cyclic_graph_example_b()
    cyclic_graph_example_c()
    acyclic_graph_example_a()
    acyclic_graph_example_b()
