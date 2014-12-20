# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 09:16:05 2014

@author: Ofim
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import math
import scipy.stats as st


def dfs(graph, start, visited=[]):
  '''recursive depth first search from start'''
  visited=visited+[start]
  for node in graph[start]:
    if not node in visited:
      visited=dfs(graph, node, visited)
  return visited



def is_tree(G):
    if nx.number_of_nodes(G) != nx.number_of_edges(G) + 1:
        return False
    return nx.is_connected(G)
    

if __name__ == '__main__':
    
    
    
    graph = nx.DiGraph()      
    
    graph.add_nodes_from(range(6))
        
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,3)
    graph.add_edge(1,4)
    graph.add_edge(2,5)
    graph.add_edge(2,6)
    
    
    
    print (is_tree(graph))
    
    a = nx.path_graph(5)
    b = nx.star_graph(5)
    c = nx.house_graph() 
    
    

    print(b.nodes())
    print(b.edges())
        
    
    print(is_tree(a))
    print(is_tree(b))
    print(is_tree(c))
    
    nx.draw_networkx(b)
    plt.show()
    
    
    
    
    #print(graph.edges())
     
    
    #check = nx.is_directed_acyclic_graph(graph)
    #print(check)
    
    
    #k = nx.degree(graph)
    #print(k)
    
    
    #graph.get_edge_data
    
    #nx.is_directed_acyclic_graph(graph)