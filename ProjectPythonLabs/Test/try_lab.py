# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 09:06:55 2014

@author: Ofim
"""

import numpy as np
from numpy.random import geometric as geom
import scipy
import math
import random

def main():
    e = 0.1 # Must be computed from confidence interval
    
    d = 10, 5
    r, c = d
    size = r*c
    prob = .4
    
    rg = geom( prob, (1+e)*int(prob*size))
    prev = np.cumsum(rg)
    
    matrix = np.zeros(size)
    matrix[ prev[prev <= size]] = 1
    matrix = np.reshape(matrix, d)
    print matrix
    
def index_to_pos(columns, index):
    a = index / columns
    b = index - columns * a
    return a, b

if __name__ == "__main__":
    main()