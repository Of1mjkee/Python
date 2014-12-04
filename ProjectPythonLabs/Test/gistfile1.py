import networkx as nx
import numpy as np
import scipy.stats as st
import math


def indices_to_edges(indices, n):
    def index_to_edge(index):
        a = index / n
        b = index - n * a
        return a, b

    return [index_to_edge(i) for i in indices]

#   Ravnomernaya generacia graffa
def uniform_edge_generator(n, p):
    distribution = np.random.uniform(0, 1, n ** 2)
    indices = np.where(distribution <= p)

    return indices_to_edges(indices, n)

#   Geometriceskaya generacia graffa
def geom_edge_generator(n, p):
    e = 0.05
    nsquared = n ** 2
    size = nsquared * p * (1 + e)

    distribution = np.random.geometric(p, size)
    indices = np.cumsum(distribution) - 1
    indices = indices[indices < nsquared]

    return indices_to_edges(indices, n)


def create_graph(graph_type, edge_generator, n, p, l):
    graph = graph_type()
    graph.add_nodes_from(range(n))
    for (u, v) in edge_generator(n, p):
        if len(graph.edges(u)) < l:
            graph.add_edge(u, v)
    return graph


def strongly_connected_components(graph):
    def find_component(start_node):
        def visit(v):
            if v not in v_dfs:
                v_dfs.add(v)
                v_root[v] = y_dfs[v] = len(v_dfs) - 1
                stack_of_nodes.append(v)

        def retract():
            stack_of_edges.pop()

            if v in components_num:
                return

            for w in graph.neighbors(v):
                if w not in components_num:
                    v_root[v] = min(v_root[w], v_root[v])

            if v_root[v] == y_dfs[v]:
                component = set()
                while True:
                    w = stack_of_nodes.pop()
                    components_num[w] = len(components)
                    component.add(w)
                    if w == v:
                        break
                components.append(component)

        stack_of_nodes = []
        stack_of_edges = [(None, start_node)]

        while len(stack_of_edges) > 0:
            u, v = stack_of_edges[-1]
            visit(v)
            neighborhood = set(graph.neighbors(v)) - v_dfs
            if len(neighborhood) == 0:
                retract()
            else:
                for w in neighborhood:
                    stack_of_edges.append((v, w))

    v_dfs = set()
    y_dfs = {}
    v_root = {}
    components_num = {}
    components = []

    for node in graph.nodes():
        if node not in v_dfs:
            find_component(node)

    return components


def update_mean(previous_mean, datum, i):
    sum_of_previous = previous_mean * (i - 1.)
    sum_of_current = sum_of_previous + datum
    return sum_of_current / i


def update_variance(mean, sum_of_squares, datum, i):
    var, sum_of_previous_squared = 0, 0
    sum_of_squares += datum ** 2
    if i > 1:
        var = (sum_of_squares - i * (mean ** 2)) / (i - 1.)
    return var, sum_of_squares


def confidence_interval(confidence, e):
    emax = e / (1 - e)
    iteration = 0
    mean = 0.
    sum_of_squares = 0.

    n, p, l = 6, 0.5, float('inf')
    graph_type = nx.DiGraph
    edge_generator = geom_edge_generator

    while True:
        iteration += 1

        graph = create_graph(graph_type, edge_generator, n, p, l)
        components = strongly_connected_components(graph)
        max_component = max([len(component) for component in components])
        test_value = max_component

        mean = update_mean(mean, test_value, iteration)
        variance, sum_of_squares = update_variance(mean, sum_of_squares, test_value, iteration)

        number_of_tests = iteration
        degrees_of_freedom = number_of_tests - 1

        standard_deviation = math.sqrt(variance)
        standard_error = standard_deviation / math.sqrt(number_of_tests)


        t = st.t(degrees_of_freedom)
        t_criteria = t.ppf((1 + confidence) / 2.)

        margin = t_criteria * standard_error

        # if interval satisfies given precision
        if margin / mean <= emax / (emax + 1):
            print "iterations: %d, interval (-, mean, +): (%f, %f, %f)" % (
                iteration, mean - margin, mean, mean + margin)
            break


def main():
    c = 0.95
    e = 0.01

    #confidence_interval(c, e)

    
if __name__ == '__main__':
    main()
