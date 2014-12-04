import numpy as np
def generate(n, p, l = float('inf')):
  matrix = np.zeros((n, n))
  sum = 0
  li = 0
  while True:
    lastRow= sum / n
    sum += np.random.geometric(p)
    row = sum /n
    if row != lastRow:
      li = 0
    if li >= l:
      continue
    if sum >= n*n:
        break;
    matrix[sum / n,sum % n] = 1
    li += 1
  return matrix
if __name__ == '__main__':
    print generate(10, 0.5)