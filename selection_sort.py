# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 15:23:25 2021

@author: adelc
"""

A=[5,4,6,3,2,1]
def selection_sort(A):
    n=len(A)
    for i in range(n):
        min_idx=i#current first element
        #look for the min element in the sequence A[i...n]
        for j in range(i,n):
            if A[min_idx]>A[j]:
                min_idx=j
        #swap the min with A[i]
        A[i],A[min_idx]=A[min_idx],A[i]
    return A
A=selection_sort(A)