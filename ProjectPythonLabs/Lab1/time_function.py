import timeit
import numpy as np
from scipy import stats
import geometric_generate
import uniform_generate
from math import sqrt


def timethis(expression, alpha, eps):
  mm = []
  
  while True:
    val = timeit.timeit(expression,number=1)
    mm.append(val)
    
    n = len(mm) - 1
    t = stats.t(n)
    tcr = t.ppf(1-alpha/2)
    
    di = tcr*np.std(mm)/sqrt(len(mm))
    
    if di/np.mean(mm) <= eps/(eps+1):
      break;
  
  mean = np.mean(mm)
  return [mean - di, mean + di]


if __name__ == '__main__':
  print timethis('import uniform_generate ; uniform_generate.get_matrix(10, 0.5)', 0.05, 1e-02)
  print timethis('import geometric_generate ; geometric_generate.get_matrix(10, 0.5)', 0.05, 1e-02)