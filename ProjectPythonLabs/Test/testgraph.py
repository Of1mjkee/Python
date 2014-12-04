# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 22:54:58 2014

@author: Ofim
"""

import networkx as nx
import numpy as np
import scipy.stats as st
import math
import pylab


def get_matrix(n, p, l=float('inf')):
  matrix = np.zeros((n,n))

  sum = 0
  li = 0
  while True:
    last_row = sum / n
    sum += np.random.geometric(p)
    row = sum /n
    
    if row != last_row:
      li = 0
      
    if li >= l:
      continue
    
    if sum >= n*n:
        break;
  
    matrix[sum / n,sum % n] = 1
    li += 1
      
    
  return matrix
      
if __name__ == '__main__':
    print get_matrix(10, 0.5)
    
    
G=nx.Graph()