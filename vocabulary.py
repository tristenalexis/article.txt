class Word:

    def __init__(self, word, position):
        self.word = word
        self.positions = [position]

    def add_position(self, position):
        self.positions.extend(position)


class Digraph(object):
    """Represents a directed graph of Node and Edge objects"""

    def __init__(self):
        self.nodes = set([])
        self.edges = {}  # must be a dict of Node -> list of edges

    def __str__(self):
        edge_strings = []
        for edges in self.edges.values():
            for edge in edges:
                edge_strings.append(str(edge))
        edge_strings = sorted(edge_strings)  # sort alphabetically
        return '\n'.join(edge_strings)  # concat edge_strings with "\n"s between them

    def get_edges_for_node(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def add_node(self, word):
        new_word = self.find(word)
        if new_word:
            new_word.add_position(word.positions)
            return new_word
        else:
            self.nodes.add(word)
            return word

    def add_edge(self, edge):
        if edge.src not in self.nodes:
            self.add_node(edge.src)

        if edge.dest not in self.nodes:
            self.add_node(edge.dest)

        if edge.src not in self.edges.keys():
            self.edges[edge.src] = [edge]
        else:
            self.edges[edge.src].append(edge)

    def find(self, word):
        for test in self.nodes:
            if word.word == test.word:
                return test

        return None


class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def get_source(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return super(Edge, self).__str__() + f'{self.src}->{self.dest} ({self.total_distance}, {self.outdoor_distance})'

