# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 14:37:09 2014

@author: Ofim
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
 
 
def is_cycle(graph):
        
    index_counter = [0]
    stack = []
    lowlinks = {}
    index = {}
    result = []
    
    def strongconnect(node):
        # set the depth index for this node to the smallest unused index
        index[node] = index_counter[0]
        lowlinks[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)
    
        # Consider successors of node
        try:
            successors = graph[node]
        except:
            successors = []
        for successor in successors:
            if successor not in lowlinks:
                # Successor has not yet been visited; recurse on it
                strongconnect(successor)
                lowlinks[node] = min(lowlinks[node],lowlinks[successor])
            elif successor in stack:
                # the successor is in the stack and hence in the current strongly connected component (SCC)
                lowlinks[node] = min(lowlinks[node],index[successor])
        
        # If node is a root node, pop the stack and generate an SCC
        if lowlinks[node] == index[node]:
            connected_component = []
            
            while True:
                successor = stack.pop()
                connected_component.append(successor)
                if successor == node: break
            component = tuple(connected_component)
            # storing the result
            result.append(component)
    
    for node in graph:
        if node not in lowlinks:
            strongconnect(node)
    
    for st in result:
        if(len(st) > 1):
            answer = "CYCLE!"
        else:
            answer = "NOT CYCLE!"
    
    return answer
    
    
graph=nx.DiGraph()
graph.add_nodes_from(range(3))
graph.add_edge(1,2)
graph.add_edge(2,3)
graph.add_edge(3,1)

print(is_cycle(graph))