# -*- coding: utf-8 -*-

import numpy as np


def next_position_uniform(p):
    a = np.random.random()
    b = 1
    while a > p:
        a = np.random.random()
        b += 1
    return b


def next_position_geometric(p):
    return np.random.geometric(p)


def dfs_visit(context, edge):
    if not context.visited_contains(edge.b):
        context.visited_add(edge.b)
        context.order_set(edge.b, context.order_count())


def dfs_retract(context, edge):
    context.stack_pop()
