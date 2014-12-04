#!/usr/bin/python
import numpy as np

def get_matrix(n, p, l=float('inf')):
  matrix = np.zeros((n,n))
  result_tup = []

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
  
    #matrix[sum / n,sum % n] = 1
    result_tup += (sum / n, sum % n)
    li += 1
      
    
  return matrix
      
if __name__ == '__main__':
    print get_matrix(10, 0.5)
    