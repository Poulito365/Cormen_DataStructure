# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:00:42 2021

@author: adelc
"""

import os
from pathlib import Path
os.chdir(Path.home()/"Desktop"/"Quant_Interview"/"Cormen")
import numpy as np
def linear_search(A):
    target=0
    position=None
    for i,elem in enumerate(A):
        if target==elem:
            position=i
            break
    ###end the search and summarize the result
    if position==None:
        print("Value Not found")
        position=np.nan
    else:
        print(f"target found at postion {i}")
    return position
#############Test Case 
A=[5,6,8,9,0,4,2,9,2]
position=linear_search(A)