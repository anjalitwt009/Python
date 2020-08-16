# -*- coding: utf-8 -*-
"""Arrays__DistinctNumber.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LpmGTYlvnwwqmxPzcSsneZ8exeRxuxuH

An array has 2*N+2 positive numbers. 2*N are pairs whereas 2 numbers are distinct and occurs exactly once. Find those numbers in ascending order.

Example 1:

*INPUT:*

1,2,3,2,1,4

*OUTPUT:*

3,4

Example 2:

*INPUT:*

2,1,3,2

*OUTPUT:*

1,3
"""

def check(A):
  n=len(A)
  D={}
  for i in range(n):
    try:
      D[A[i]]+=1
    except:
      D[A[i]]=1
  A=[]
  for key in D.keys():
    if D[key] == 1:
      A.append(key)
  x=A[0]
  y=A[1]
  if A[0]>A[1]:
    x=A[1]
    y=A[0]
  print(x,y)

A=list(map(int,input("Enter the list: ").split(' ')))
check(A)