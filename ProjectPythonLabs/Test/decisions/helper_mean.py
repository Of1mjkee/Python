# -*- coding: utf-8 -*-

import time
import numpy as np
import scipy.stats as sp


class MeanCounter(object):

    def __init__(self):
        self._n = 0.0
        self._mean = 0.0
        self._mean_sqr = 0.0

    def push(self, current):
        self._n += 1.0
        coef = ((self._n - 1.0) / self._n)
        self._mean = self._mean * coef + current / self._n
        self._mean_sqr = self._mean_sqr * coef + current * current / self._n

    def n(self):
        return self._n

    def mean(self):
        return self._mean

    def interval(self):
        if self._n < 2:
            return -1
        a = self._mean_sqr * self._n / (self._n - 1)
        b = self._mean * self._mean * self._n / (self._n - 1)
        disp = a - b
        dist = 0
        if self._n < 30:
            dist = sp.t.ppf(1 - 0.15 / 2, self._n - 1)
        else:
            dist = sp.norm.ppf(1 - 0.15 / 2)
        return dist * disp / np.sqrt(self._n)


class TimeRating(object):

    def __init__(self):
        self._time = None
        self._mean = MeanCounter()

    def start(self):
        self._time = time.time()

    def stop(self):
        current = (time.time() - self._time)
        self._mean.push(current)

    def n(self):
        return self._mean.n()

    def mean(self):
        return self._mean.mean()

    def interval(self):
        return self._mean.interval()
