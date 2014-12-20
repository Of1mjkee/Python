# -*- coding: utf-8 -*-

import numpy as np
import helper_matrix as hm
import sets as s


class TarjanContext(object):

    def __init__(self):
        pass

    def init(self, n):
        self._root = np.repeat(-1, n)
        self._nodes = []
        self._components = np.repeat(-1, n)
        self._components_count = 0
        self._closure_comp = {}

    def root_set(self, index, value):
        self._root[index] = value

    def root_get(self, index):
        return self._root[index]

    def nodes_push(self, index):
        self._nodes.append(index)

    def nodes_peek(self):
        return self._nodes[-1]

    def nodes_pop(self):
        return self._nodes.pop()

    def nodes_count(self):
        return len(self._nodes)

    def components_set(self, index, value):
        self._components[index] = value

    def components_get(self, index):
        return self._components[index]

    def components_count(self):
        return self._components_count

    def components_count_inc(self):
        self._components_count += 1

    def rebuild_components(self):
        bounds = list(range(self._components.size))
        for i in bounds:
            self._components[i] = self._components[self._root[i]]

    def components_max(self):
        result = 0
        for i in np.unique(self._components):
            result = max(result, sum(self._components == i))
        return result

    def closure(self):
        n = self._components.size
        result = hm.Matrix(n)
        bounds = list(range(n))
        for a in self._closure_comp:
            for i in bounds:
                for j in bounds:
                    if (self._components[i] == a) and (self._components[j] == a):
                        result.add(i, j)
            for b in self._closure_comp[a]:
                for i in bounds:
                    for j in bounds:
                        if (self._components[i] == a) and (self._components[j] == b):
                            result.add(i, j)
        return result

    def closure_add(self, i, j):
        if i not in self._closure_comp:
            self._closure_comp.update({i: s.Set()})
        self._closure_comp[i].add(j)
        if j in self._closure_comp:
            self._closure_comp[i] = self._closure_comp[i].union(self._closure_comp[j])


def tarjan_visit(context, edge):
    if not context.visited_contains(edge.b):
        context.visited_add(edge.b)
        context.order_set(edge.b, context.order_count())
        context.additional().root_set(edge.b, edge.b)
        context.additional().nodes_push(edge.b)


def tarjan_retract(context, edge):
    context.stack_pop()
    if context.additional().components_get(edge.b) != -1:
        return
    root = context.additional().root_get(edge.b)
    order = context.order_get(root)
    children = context.matrix().children(edge.b)
    for i in children:
        if (context.additional().components_get(i) == -1):
            candidate = context.additional().root_get(i)
            candidate_order = context.order_get(candidate)
            if (candidate_order < order):
                root = candidate
                order = candidate_order
    context.additional().root_set(edge.b, root)
    if root == edge.b:
        context.additional().components_count_inc()
        curr_comp = context.additional().components_count()
        while True:
            i = context.additional().nodes_pop()
            context.additional().components_set(i, curr_comp)
            for j in context.matrix().children(i):
                next_comp = context.additional().components_get(j)
                if next_comp != -1:
                    context.additional().closure_add(curr_comp, next_comp)
            if (root == i):
                break
