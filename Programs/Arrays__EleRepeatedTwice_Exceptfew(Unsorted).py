# -*- coding: utf-8 -*-
"""Arrays__eleRepeatedTwice_exceptFew(Unsorted).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X2xegraFXBEr38N2ULzsi8OAlesxHEn1

There is an unsorted array with every element repeated twice except one. Find that element. Also define a function if more then one element occurs only once.

Example 1:

*INPUT*:

A=[1,5,5,2,3,1,3]

*OUTPUT*:

2

Example 2:

*INPUT*:

A=[1,5,4,1,2]

*OUTPUT*:

2,5,4
"""

def single_rep(A,n):
  D={}
  C=[]
  for ele in A:
    try:
      D[ele] +=1
    except:
      D[ele] = 1

  for key in D:
    if (D[key]==1):
      C.append(key)
  
  print(C)

print("Enter the array elements unsorted order")
A=list((input().split(' ')[:n]))
print(A)
n=len(A)
single_rep(A,n)