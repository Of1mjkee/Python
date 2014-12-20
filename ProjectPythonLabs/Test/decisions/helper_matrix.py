# -*- coding: utf-8 -*-

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Edge(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b


class DFSContext(object):

    def __init__(self, matrix, additional):
        self._matrix = matrix
        self._stack = []
        self._order = np.repeat(-1, matrix.n())
        self._order_count = 0
        self._visited = np.empty(0, dtype=int)
        self._additional = additional
        if self._additional is not None:
            self._additional.init(matrix.n())

    def matrix(self):
        return self._matrix

    def stack_push(self, e):
        self._stack.append(e)

    def stack_peek(self):
        return self._stack[-1]

    def stack_pop(self):
        return self._stack.pop()

    def stack_size(self):
        return len(self._stack)

    def order_count(self):
        return self._order_count

    def order_set(self, index, value):
        if self._order[index] == -1:
            self._order_count += 1
        self._order[index] = value

    def order_get(self, index):
        return self._order[index]

    def visited_add(self, index):
        self._visited = np.append(self._visited, [index])

    def visited_contains(self, index):
        return (self._visited == index).any()

    def visited_list(self):
        return self._visited

    def additional(self):
        return self._additional


class Matrix(object):

    def __init__(self, n):
        self._n = n
        self._data = np.zeros((n, n))

    def n(self):
        return self._n

    def add(self, i, j):
        self._data[i, j] = 1

    def get(self, i, j):
        return self._data[i, j]

    def set(self, i, j, value):
        self._data[i, j] = value

    def add_edge(self, e):
        self._data[e.a, e.b] = 1

    def get_edge(self, e):
        return self._data[e.a, e.b]

    def set_edge(self, e, value):
        self._data[e.a, e.b] = value

    def add_right(self, i, indices):
        for j in indices:
            self._data[i, j] = 1

    def add_left(self, indices, j):
        for i in indices:
            self._data[i, j] = 1

    def children(self, u):
        result = np.empty(0)
        for i in range(self._n):
            if self._data[u, i] != 0:
                result = np.append(result, [i])
        return result

    def parents(self, v):
        result = np.empty(0)
        for i in range(self._n):
            if self._data[i, v] != 0:
                result = np.append(result, [i])
        return result

    def warshall(self):
        result = Matrix(self._n)
        result._data = self._data.copy()
        bounds = list(range(self._n))
        for k in bounds:
            for i in bounds:
                for j in bounds:
                    if (result._data[i, k] != 0) and(result._data[k, j] != 0):
                        result._data[i, j] = 1
        return result

    def dfs(self, root, visit, retract, additional=None):
        result = DFSContext(self, additional)
        result.stack_push(Edge(-1, root))
        while result.stack_size() > 0:
            current = result.stack_peek()
            visit(result, current)
            addition = np.setdiff1d(self.children(current.b), result.visited_list())
            if len(addition) == 0:
                retract(result, current)
            else:
                for i in addition:
                    result.stack_push(Edge(current.b, i))
        return result

    def visualize(self, labels=None):
        magic = list(range(self._n))
        current = nx.DiGraph()
        current.add_nodes_from(magic)
        for i in magic:
            for j in magic:
                if self._data[i, j] != 0:
                    current.add_edge(i, j)
        positions = nx.spring_layout(current)
        nx.draw_networkx_nodes(current, positions, node_size=900)
        nx.draw_networkx_edges(current, positions, arrows=True)
        nx.draw_networkx_labels(current, positions, labels=labels)
        plt.show()


def generate_matrix(n, p, l, f):
    result = Matrix(n)
    m = l * 2 + 1
    if m > n:
        m = n
    edge = m * n
    pos = -1
    while pos < edge:
        pos += f(p)
        if (pos < edge):
            i = pos / m
            j = ((i - l) + pos % m) % n
            result.add(i, j)
    return result


def check_matrix(matrix):
    test = matrix.warshall()
    bounds = list(range(matrix.n()))
    for i in bounds:
        if test.get(0, i) == 0:
            return False
    return True