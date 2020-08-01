# -*- coding: utf-8 -*-
"""BitManipulation__Set_kth_Bit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CTWl1dheyJvwt1p4P7nafMrRvH1wJ8f8

Set the kth bit. LSB starts from 0, next last bit at position 1, and so on.

Example 1:

*INPUT:*

10,2

*OUTPUT:*

14

Example 2:

*INPUT:*

15,3

*OUTPUT:*

15
"""

def set_kth(N,k):
  bin_num=[]
  num=[]
  while (N>0):
    x=N%2
    bin_num.append(x)
    N=N//2
  for i in range(len(bin_num)-1,-1,-1):
    if i==(k):
      num.append(1)
    else:
      num.append(bin_num[i])
  new_str=str(num)
  value=0
  x=len(num)-1
  for i in range(len(num)):
    value=value+(2**x)*num[i]
    x-=1
  print(value)

print("Enter the integer value:")
N=int(input())
print("Enter 'k': ")
k=int(input())
set_kth(N,k)