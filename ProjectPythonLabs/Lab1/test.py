# -*- coding: utf-8 -*-
"""
Created on Thu Oct 09 23:29:04 2014

@author: Ofim
"""
import numpy as np

p = 0.35

a = np.random.geometric(p , size=10000).sum()
print(a/10000)