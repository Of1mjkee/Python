# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 23:36:38 2014

@author: Ofim
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import math
import scipy.stats as st

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
  
def dfs(graph, start, visited=[]):
  '''recursive depth first search from start'''
  visited=visited+[start]
  for node in graph[start]:
    if not node in visited:
      visited=dfs(graph, node, visited)
  return visited

def strongly_connected_components(graph):
    
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
    
    return result
    
def update_mean(previous_mean, datum, i):
    sum_of_previous = previous_mean * (i - 1.)
    sum_of_current = sum_of_previous + datum
    return sum_of_current / i


def update_variance(mean, sum_of_squares, datum, i):
    var, sum_of_previous_squared = 0, 0
    sum_of_squares += datum ** 2
    if i > 1:
        var = (sum_of_squares - i * (mean ** 2)) / (i - 1.)
    return var, sum_of_squares

def confidence_interval(confidence, e):
    emax = e / (1 - e)
    iteration = 0
    mean = 0.
    sum_of_squares = 0.

    n, p, l = 6, 0.5, float('inf')
    #graph_type = nx.DiGraph
    #edge_generator = geom_edge_generator

    while True:
        iteration += 1

        n, p = 7, 0.2
        connections = generate_geometric(n, p)
    
        graph = create_graph(connections)
        #graph = create_graph(co)
        components = strongly_connected_components(graph)
        max_component = max([len(component) for component in components])
        test_value = max_component

        mean = update_mean(mean, test_value, iteration)
        variance, sum_of_squares = update_variance(mean, sum_of_squares, test_value, iteration)

        number_of_tests = iteration
        degrees_of_freedom = number_of_tests - 1

        standard_deviation = math.sqrt(variance)
        standard_error = standard_deviation / math.sqrt(number_of_tests)


        t = st.t(degrees_of_freedom)
        t_criteria = t.ppf((1 + confidence) / 2.)

        margin = t_criteria * standard_error

        # if interval satisfies given precision
        if margin / mean <= emax / (emax + 1):
            print "iterations: %d, interval (-, mean, +): (%f, %f, %f)" % (
                iteration, mean - margin, mean, mean + margin)
            break

if __name__ == '__main__':
    
    n, p = 7, 0.2
    connections = generate_geometric(n, p)
    
    graph = create_graph(connections)    
    
    pos = nx.circular_layout(graph)
    
    plt.show()
    print("DFS: ", dfs(graph, 0))  
    result = strongly_connected_components(graph)    
    print("SCC: ", result)
    #print(sorted(graph.nodes()))
      
    nx.draw(graph, pos, node_size=800, node_color='b')
    for i in result:
        nx.draw(graph, pos, node_size=800, node_color='r', nodelist=i) 
        
    c = 0.95
    e = 0.01

    confidence_interval(c, e)
    
    
    