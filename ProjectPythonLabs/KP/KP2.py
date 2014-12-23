# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 18:03:15 2014

@author: Ofim
"""

import networkx as nx
 
 
def get_incoming_nodes(graph, node):
    return set([u for u, v in graph.in_edges([node])])
 
 
def upper_neighborhood(graph, node):
    return get_incoming_nodes(graph, node) | {node}
 
 
def upper_neighborhood_of_set(graph, X):
    result = set()
    for x in X:
        result |= upper_neighborhood(graph, x)
    return result
 
 
def own_upper_neighborhood(graph, u, X):
    return upper_neighborhood(graph, u) - upper_neighborhood_of_set(graph, X - {u})
 
 
def check(graph, check_nodes):
    for node in check_nodes:
        if len(own_upper_neighborhood(graph, node, check_nodes)) == 0:
            return False
    return True
 
 
_graph = nx.DiGraph([
    (1, 2), (3, 1), (4,2)
])

nx.draw(_graph)
_check_nodes = {3, 4}
 
print check(_graph, _check_nodes)