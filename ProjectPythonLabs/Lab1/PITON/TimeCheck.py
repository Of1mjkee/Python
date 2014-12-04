import timeit
import numpy as np
from scipy import stats
#import geometric_generate
#import uniform_generate
from math import sqrt
def getTime(expression, alpha, eps):
  mat = []
  
  while True:
    time = timeit.timeit(expression, number=1)
    mat.append(time)
    n = len(mat) - 1
    t = stats.t(n)
    tcr = t.ppf(1-alpha/2)
    di = tcr*np.std(mat)/sqrt(len(mat))
    if di/np.mean(mat) <= eps/(eps+1):
      break;
  mean = np.mean(mat)
  return [mean - di, mean + di]

if __name__ == '__main__':
  print getTime('import GenerateSteady ; GenerateSteady.generate(10, 0.5)', 0.05, 1e-02)
  print getTime('import GenerateGeometric ; GenerateGeometric.generate(10, 0.5)', 0.05, 1e-02)