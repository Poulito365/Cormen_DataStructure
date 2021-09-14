# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:31:40 2021

@author: adelc
"""

###################Chapter 2 Cormen#############
def insertion_sort(A):
    for j in range(1,len(A)):
        #locate the key
        key=A[j]
        #insert the key in the sorted array
        i=j-1#down neighbours of the key
        ####move the key down 
        while i>=0 and key<A[i]:
            A[i+1]=A[i]
            i=i-1
            A[i+1]=key
    return A
##########Test Case 1##########
A=[5,2,4,6,1,3]
A=insertion_sort(A)
########Test Case 2#####
B=[31,41,59,26,41,58]
B=insertion_sort(B)