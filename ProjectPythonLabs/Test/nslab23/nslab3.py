# -*- coding: utf-8 -*-


import networkx as nx
import numpy as np

#from examples import tarjan_graph as tg
from nslab1 import getMatrixL as gm
from nslab2 import Tarjan_graph as tg

class Warshall:
    
    def transit(self, G):
        for k in range(len(G.nodes())):
            for i in range(len(G.nodes())):
                if i != k and (i, k) in G.edges():
                    #print "for", (i, k)
                    for j in range(len(G.nodes())):
                        if (k, j) in G.edges() and (i, j) not in G.edges():
                            G.add_edge(i, j)
                            #print "added",(i,j)


if __name__ == '__main__':
    GR = Warshall(); 
    g = nx.DiGraph( np.asarray( gm(8, 0.4, 2) ) )  
    GR.transit(g)
    nx.draw(g)