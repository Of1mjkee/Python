# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 09:26:24 2014

@author: Ofim
"""
#c = [a[0] + b[0], a[0] + b[1], .., a[0] + b[4], a[1] + b[0], ...]
import numpy as np
from numpy.random import geometric as geom

def main():
    e = 0.1
    
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

r = range(1,20)
print r
print r[0]


def getR(k):
    if k == 0:
        return r[0]
    result = (k-1/k) * getR(k-1) + 1/k * r[k]
    return result
    
    
    
def index_to_pos(columns, index):
    a = index / columns
    b = index - columns * a
    return a, b

if __name__ == "__main__":
    main()
    a = np.array([1,2,3,4,5])
    print a.astype(float)    

r = [ 0.229, 0.913, 0.356, 0.091, 0.776, 
      0.667, 0.672, 0.780, 0.307, 0.612 ]
n = len(r)
av = np.mean(r)
print "Average:", av
av = sum(r) / n
print "Average:", av
    
av = r[0]
for k in xrange(1, n):
    av = float(k) / (k+1) * av + 1. / (k+1) * r[k]
print "Average:", av
    
    
    
    