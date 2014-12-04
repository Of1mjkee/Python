# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 23:36:38 2014

@author: Ofim
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def create_graph(links):
    # extract nodes from graph
    nodes = range(n)
    
    # create networkx graph
    G=nx.DiGraph()
    
    # add nodes
    for node in nodes:
        G.add_node(node)
        
    # add edges
    for edge in links:
        G.add_edge(edge[0], edge[1])
        
    return G

    

def generate_uniform(n, p, l=float('inf')):
  result_tup = []

  for i in range(0,n):
    li = 0
    for j in range(0,n):
      if np.random.uniform() > p:
        t = (i, j)
        result_tup.append(t)
        li += 1
        
      if li >= l:
        break;
    
  return result_tup

def generate_geometric(n, p, l=float('inf')):
  result_tup = []
  sum = 0
  li = 0
  while True:
    last_row = sum / n
    sum += np.random.geometric(p)
    row = sum / n
    
    if row != last_row:
      li = 0
      
    if li >= l:
      continue
    
    if sum >= n*n:
        break;
  
    t = (sum / n, sum % n)
    result_tup.append(t)
    li += 1
      
  return result_tup
  
def dfs(graph, start, path=[]):
  '''recursive depth first search from start'''
  path=path+[start]
  for node in graph[start]:
    if not node in path:
      path=dfs(graph, node, path)
  return path


  
      
if __name__ == '__main__':
    
    n, p = 10, 0.9    
    connections = generate_uniform(n, p)
    
    graph = create_graph(connections)    
    
    pos = nx.circular_layout(graph)
    
    nx.draw(graph, pos, node_size=1500, node_color='b')

    plt.show()
    print(dfs(graph, 0))  
    
    