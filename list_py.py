# -*- coding: utf-8 -*-
"""list.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CbA669xNzwaqdh_1D9XGsdbC7Z52LZev
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

import numpy as np
 
def fun(start, end, step):
    num = np.linspace(start, end,(end-start)
                      *int(1/step)+1).tolist()
    return [round(i, 2) for i in num]
     
 
print(fun(1,5,0.5))
