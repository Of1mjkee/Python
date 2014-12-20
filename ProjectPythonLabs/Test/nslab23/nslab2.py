# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 10:53:36 2014

@author: varie_000
"""
import networkx as nx
import numpy as np
import nslab1 as ns1

from examples import tarjan_graph as tg


class Tarjan_graph:

    def __init__(self):
        self.count = 8
        self.root = [-1]*self.count
        self.s=[]
        self.sv=[]
        self.ctmp=0
        self.c=[0]*self.count
        self.Vdfs = []
        self.ydfs = [0]*self.count
       
    def visit(self,v):
        if((v in self.Vdfs)==0):
            self.Vdfs.append(v)
            self.ydfs[v] = len(self.Vdfs)
            self.root[v]=v
            self.sv.append(v)
        
    def retract(self,v,G):
        global ctmp
        if(len(self.s)!=0):
            self.s.pop()
        nei = G.successors(v)
        #print v, nei    
        for el in nei:
            if(self.ydfs[self.root[v]]>self.ydfs[self.root[el]] and self.c[el]==0):
                self.root[v] = self.root[el]
            nei2 = G.successors(el)
            for el2 in nei2:
                G.add_edge(v, el2)
        if(self.root[v]==v):
            self.ctmp=self.ctmp+1
            while True:
                if(len(self.sv)!=0):
                    wt = self.sv.pop()
                    self.c[wt] = self.ctmp
                    nei = G.successors(v)
                    for el in nei:
                        G.add_edge(wt, el)
                    if(wt==v):
                        break
            
    def DeepFirstSearch(self,G,v):
        self.s.append([v, v])
        while(len(self.s)!=0):
            t=self.s[-1]
            self.visit(t[1])
            result = G.successors(t[1])
            for el in self.Vdfs:
                if el in result:
                    result.remove(el)
            if(len(result)==0):
                self.retract(t[1],G)
            else:
                for element in result:
                    self.s.append([t[1],element])
            #print t, self.s   
    
    def totalSearch(self,G):
        for a in range(0, self.count):
            if self.c[a] == 0:
                self.DeepFirstSearch(G,a);
        
if __name__ == '__main__':
    #print "test1"
    GR = Tarjan_graph(); 
    g = nx.DiGraph( np.asarray( ns1.getMatrixL(GR.count, 0.4, 2) ) )
    #print "test2"
    GR.totalSearch(g)
    #print "test3"
    nx.draw(g)
    print GR.c
