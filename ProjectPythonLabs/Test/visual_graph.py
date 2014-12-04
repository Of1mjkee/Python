# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 22:29:20 2014

@author: Ofim
"""

import networkx as nx
import numpy as np
import scipy.stats as st
import math
import pylab


def indices_to_edges(indices, n):
    def index_to_edge(index):
        a = index / n
        b = index - n * a
        return a, b

    return [index_to_edge(i) for i in indices]

def geom_edge_generator(n, p):
    e = 0.05
    nsquared = n ** 2
    size = nsquared * p * (1 + e)

    distribution = np.random.geometric(p, size)
    indices = np.cumsum(distribution) - 1
    indices = indices[indices < nsquared]

    return indices_to_edges(indices, n)

def create_graph(graph_type, edge_generator, n, p, l):
    graph = graph_type()
    graph.add_nodes_from(range(n))
    for (u, v) in edge_generator(n, p):
        if len(graph.edges(u)) < l:
            graph.add_edge(u, v)
    return graph



n, p, l = 6, 0.5, float('inf')
graph_type = nx.DiGraph
edge_generator = geom_edge_generator


graph = create_graph(graph_type, edge_generator, n, p, l)

pos=nx.spring_layout(graph)
nx.draw_networkx_edge_labels(graph,pos)
nx.draw(graph,pos,node_size=1500)
pylab.show()


