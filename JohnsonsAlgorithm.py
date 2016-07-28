# -*- coding: utf-8 -*-
"""
Created on Mon May 30 04:58:21 2016

@author: Cameron
"""
import networkx as nx
import networkx_cycles as nxl
import multiprocessing
import numpy as np
import time
from alist2full import alist2full

n=0
if   n==0: matrix_input = 'PEGReg252x504';      max_cycle_length = 12
elif n==1: matrix_input = 'PEGReg504x1008';     max_cycle_length = 10  
elif n==2: matrix_input = 'PEGirReg252x504';    max_cycle_length = 10
elif n==3: matrix_input = 'PEGirReg504x1008';   max_cycle_length = 14
elif n==4: matrix_input = '8000.4000.3.483';    max_cycle_length = 10
elif n==5: matrix_input = '10000.10000.3.631';  max_cycle_length = 10
elif n==6: matrix_input = '816.3.174';          max_cycle_length = 10
elif n==7: matrix_input = '816.55.178';         max_cycle_length = 10
        

matrix = alist2full('codes/'+matrix_input)
matrix = np.array(matrix,dtype=np.bool)
nonz = matrix.nonzero()

num_parity_nodes = matrix.shape[0]
parity_nodes=[[] for i in xrange(num_parity_nodes)]
for index,k in enumerate(nonz[0]):
    parity_nodes[k].append(nonz[1][index])
    
num_variable_nodes = matrix.shape[1]
variable_nodes=[[] for i in xrange(num_variable_nodes)]
for index,k in enumerate(nonz[1]):
    variable_nodes[k].append(nonz[0][index])

G = nx.DiGraph()
for idx,m in enumerate(parity_nodes):
    for k in m:
        G.add_edge(idx, int(k+num_parity_nodes))
        G.add_edge(int(k+num_parity_nodes), idx)

for idx,m in enumerate(variable_nodes):
    for k in m:
        G.add_edge(idx+num_parity_nodes, k)
        G.add_edge(k,idx+num_parity_nodes)

timer = time.clock()

print nxl.recursive_simple_cycles(G, max_cycle_length)
print time.clock()-timer