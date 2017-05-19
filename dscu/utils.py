"""
file: utils
author: fupeng
date: 2017/5/5


"""
from graphviz import Digraph


def draw_graph(nodes, view=False):
    graph = Digraph("G", format="pdf", graph_attr={'lwidth': '20', 'ratio': 'compress'})
    edges = []
    _nodes = []
    for node in nodes:
        graph.node(node.name, node.name)
        _nodes.append(node.name)
        if node.father_nodes:
            for father_node in node.father_nodes:
                if father_node.name not in nodes:
                    graph.node(father_node.name, father_node.name)
                    print father_node.name
                    _nodes.append(father_node.name)
                graph.edge(father_node.name, node.name)
    if view:
        graph.view()



