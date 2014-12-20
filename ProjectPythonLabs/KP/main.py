import networkx as nx


def get_incoming_nodes(graph, node):
    return [u for u, v in graph.in_edges([node])]


def is_tree(graph):
    flag = nx.is_directed_acyclic_graph(graph)
    if flag == False:
        return False
    l = [v for u, v in graph.edges()]
    s = set(l)
    if len(s) == len(l):
        return True
    return False
    


def get_parents(graph, node):
    node_parents = [node]
    current = node
    while True:
        p = get_incoming_nodes(graph, current)
        if len(p) == 0:
            break
        current = p[0]
        node_parents.append(current)
    return node_parents

#graph = nx.DiGraph([(1, 2)])
u = 4
v = 6

graph = nx.DiGraph()      
    
graph.add_nodes_from(range(7))

        
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1,3)
graph.add_edge(1,4)
graph.add_edge(5,2)
graph.add_edge(2,6)
graph.add_edge(5,6)
graph.add_edge(6,2)

nx.draw(graph)


if is_tree(graph):
    u_parents = get_parents(graph, u)
    v_parents = get_parents(graph, v)
    for i in u_parents:
        if i in v_parents:
            print i
            break
else:
    print("NOT TREE")