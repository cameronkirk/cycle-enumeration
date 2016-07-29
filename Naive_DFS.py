import time
import math
import numpy as np


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
from alist2full import alist2full\

def main():
    n=0; z=1
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
    
    if z==1:
        num_parity_nodes = matrix.shape[0]
        num_variable_nodes = matrix.shape[1]
    else:
        num_parity_nodes = matrix.shape[1]
        num_variable_nodes = matrix.shape[0]        

    timer = time.clock()
    
    nonz = matrix.nonzero()
    parity_nodes=[[] for i in xrange(num_parity_nodes)]
    variable_nodes=[[] for i in xrange(num_variable_nodes)]
    if z==1:
        for index,k in enumerate(nonz[0]):
            parity_nodes[k].append(nonz[1][index])
        for index,k in enumerate(nonz[1]):
            variable_nodes[k].append(nonz[0][index])
    else:
        for index,k in enumerate(nonz[1]):
            parity_nodes[k].append(nonz[0][index])
        for index,k in enumerate(nonz[0]):
            variable_nodes[k].append(nonz[1][index])
    
    parity_nodes = [[int(x) for x in y] for y in parity_nodes]
    variable_nodes = [[int(x) for x in y] for y in variable_nodes]

    DFS([0,1,variable_nodes,parity_nodes,max_cycle_length])

    print time.clock()-timer
   
def DFS(Chunk):
    def dfs(current_node,depth):
#        counter2=0
        for x in variable_nodes[current_node]: 
#            counter2 += 1
            if not visited_parity[x]:
                visited_parity[x]=True
                for y in parity_nodes[x]:
#                        counter2 += 1
                        if y==root_node:
                                cycles[depth]+=1
                        elif not visited_variable[y]:
                            if depth+2 <max_depth:
                                visited_variable[y]=True
                                dfs(y,depth+2)
                                visited_variable[y]=False                               
                            else:
                                for w in variable_nodes[y]:
#                                    counter2 += 1
                                    if not visited_parity[w]:
                                        for z in parity_nodes[w]:
                                            if z==root_node:
                                                    cycles[depth+2]+=1
                visited_parity[x]=False    

    Chunk_Index     = Chunk[0]
    Total_Chunks    = Chunk[1]
    variable_nodes  = Chunk[2]
    parity_nodes    = Chunk[3]
    max_depth       = Chunk[4]
    cycles = np.array([0]*(max_depth+1))

    num_variable_nodes = len(variable_nodes)
    num_parity_nodes = len(parity_nodes)
    visited_parity = [False]*len(parity_nodes)
    visited_variable = [False]*len(variable_nodes)  

    for a in range(num_variable_nodes):
         root_node = a
         for n in variable_nodes[a][:]:
            visited_variable[a]=True
            if visited_parity[n]==False:
                visited_parity[n] = True
                for b in parity_nodes[n]:
                    if visited_variable[b]==False:
                        visited_variable[b]=True
                        dfs(b,4)
                        visited_variable[b]=False
                visited_parity[n]=False
            visited_variable[a]=False 
         variable_nodes[a]=[]
    print cycles/2
    
if __name__=='__main__':
    main()