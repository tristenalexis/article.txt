import string

from vocabulary import Word, Digraph, Edge

graph = Digraph()


def load_map(ok):

    with open(ok) as f:
        previous_word = None
        if previous_word:
            graph.add_edge(Edge(previous_word, node))
            previous_word = node
            print(graph)
        for i, line in enumerate(f):
            table = str.maketrans(dict.fromkeys(string.punctuation))
            line = line.translate(table)
            for w, word in enumerate(line.split()):
                print(i, w, word)
                node = graph.add_node(Word(word.lower(), (i, w)))


load_map('ok')
