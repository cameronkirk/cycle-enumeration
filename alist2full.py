# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:38:22 2015

@author: Cameron
"""
import numpy as np
from pdb import set_trace as breakpoint

"""
Take an example matrix

1 0 1
0 0 1

in alist format we would have:

2 3     number of rows and columns
1.5 1   average weighting of each row or column?
2 1     weights of each row
1 0 2   weights of each column

1       first column: one at index 1
-       second column: no ones
1 2     third column: one at index 1 and 2

1 3     first row: one at index 1 and 3
3       second row: one at index 3

So, to convert we generate a zeros matrix using the first line, disregard the
weighting information, then fill in the matrix using the positions of the ones in rows

So:
N x K matrix, ie. N/K rate code has

4 LINES OF CLASSIFICATION
K LINES FOR THE ONES IN EACH COLUMN
N LINES FOR THE ONES IN EACH ROW

note that python indexing starts at zero.
"""


def alist2full(workfile):
    """Converts a-list format to a sparse matrix
    
    """
    f = open(workfile, 'r')
    
    for index, line in enumerate(f): #print out each line, and count the line number
        if index == 0: #if we have the first line, separate the components, and generate a zeroes matrix of that size
            rows = int(line.split()[1]) #take first element of first line, convert to int, this is the number of rows
            columns = int(line.split()[0]) #take second element, convert to int, this is the number of columns
            fullMatrix = np.zeros((rows, columns),dtype=np.bool)
#        if index == 
        #We fill in the matrix, using the placement of ones in each column in the alist file ()
        if index in range(4,columns+4):
#            print index, columns
            vectorFromString = map(int,line.split())
#            print vectorFromString
            for index2,k in enumerate(vectorFromString):
                
                if index2>0:
                    if k>0:
                        fullMatrix[k-1,index-4] = 1 #dont forget to re-index (hence we use k-1)
                else:
                    fullMatrix[k-1,index-4] = 1 #dont forget to re-index (hence we use k-1)

            
    return fullMatrix