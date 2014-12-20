# -*- coding: utf-8 -*-

import helper_matrix as hm
import helper_functions as hf
import helper_tarjan as ht
import helper_tarjan_optimized as hto
import helper_mean as hmean

if __name__ == '__main__':
    n = 5
    p = 0.3
    l = 100

# --- DFS --- #
    matrix = hm.Matrix(n)
    while not hm.check_matrix(matrix):
        matrix = hm.generate_matrix(n, p, l, hf.next_position_geometric)
    result = matrix.dfs(0, hf.dfs_visit, hf.dfs_retract)
    labels = {}
    for i in range(n):
        labels.update({i: result.order_get(i)})
    matrix.visualize(labels)

# --- Tarjan --- #
    matrix = hm.Matrix(n)
    while not hm.check_matrix(matrix):
        matrix = hm.generate_matrix(n, p, l, hf.next_position_geometric)
    result = matrix.dfs(0, ht.tarjan_visit, ht.tarjan_retract, additional=ht.TarjanContext())
    labels = {}
    for i in range(n):
        labels.update({i: str(result.additional().components_get(i))})
    matrix.visualize(labels)

# --- Maximal --- #
    counter = hmean.MeanCounter()
    while (counter.n() < 2) or (counter.interval() > 0.5):
        matrix = hm.Matrix(n)
        while not hm.check_matrix(matrix):
            matrix = hm.generate_matrix(n, p, l, hf.next_position_geometric)
        try:
            result = matrix.dfs(0, ht.tarjan_visit, ht.tarjan_retract, additional=ht.TarjanContext())
            counter.push(result.additional().components_max())
            print counter.mean(), '~', counter.interval()
        except:
            pass
    print 'result:', counter.mean(), '~', counter.interval()

# --- Warshall transitive closure --- #
    matrix = hm.generate_matrix(n, p, l, hf.next_position_geometric)
    result = matrix.warshall()
    matrix.visualize()
    result.visualize()

# --- Tarjan transitive closure --- #
    matrix = hm.Matrix(n)
    while not hm.check_matrix(matrix):
        matrix = hm.generate_matrix(n, p, l, hf.next_position_geometric)
    result = matrix.dfs(0, ht.tarjan_visit, ht.tarjan_retract, additional=ht.TarjanContext()).additional().closure()
    matrix.visualize()
    result.visualize()

# --- Tarjan transitive closure optimized --- #
    matrix = hm.Matrix(n)
    while not hm.check_matrix(matrix):
        matrix = hm.generate_matrix(n, p, l, hf.next_position_geometric)
    result = matrix.dfs(0, hto.tarjan_visit, hto.tarjan_retract, additional=hto.TarjanContext()).additional().closure()
    matrix.visualize()
    result.visualize()

# --- Computing ---
    first = hmean.TimeRating()
    second = hmean.TimeRating()
    third = hmean.TimeRating()
    while third.n() < 50:
        matrix = hm.Matrix(n)
        while not hm.check_matrix(matrix):
            matrix = hm.generate_matrix(n, p, l, hf.next_position_geometric)
        try:
            first.start()
            matrix.dfs(0, ht.tarjan_visit, ht.tarjan_retract, additional=ht.TarjanContext())
            first.stop()
            second.start()
            matrix.dfs(0, hto.tarjan_visit, hto.tarjan_retract, additional=hto.TarjanContext())
            second.stop()
            third.start()
            matrix.warshall()
            third.stop()
        except:
            pass
    print 'warshal         :', third.mean(), '~', third.interval()
    print 'tarjan          :', first.mean(), '~', first.interval()
    print 'tarjan optimized:', second.mean(), '~', second.interval()