import numpy as np
def generate(n, p, l = float('inf')):
  matrix = np.zeros((n, n))
  for x in range(0, len(matrix)):
    li = 0
    for y in range(0, len(matrix[x])):
      if np.random.uniform() > p:
        matrix[x,y] = 1
        li += 1
      if li >= l:
        break;
  return matrix
      
if __name__ == '__main__':
    print generate(10, 0.5)