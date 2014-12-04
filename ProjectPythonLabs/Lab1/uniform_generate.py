#!/usr/bin/python

#>>> timeit.timeit('import geometric_generate ; geometric_generate.get_matrix()',number=1000)
#0.035665035247802734
#>>> timeit.timeit('import uniform_generate ; uniform_generate.get_matrix()',number=1000)
#0.04297304153442383

import numpy as np

def get_matrix(n, p, l=float('inf')):
  matrix = np.zeros((n,n))

  for i in range(0,len(matrix)):
    li = 0
    for j in range(0,len(matrix[i])):
      if np.random.uniform() > p:
        matrix[i,j] = 1
        li += 1
        
      if li >= l:
        break;
    
  return matrix
      
if __name__ == '__main__':
    print get_matrix(10, 0.5)