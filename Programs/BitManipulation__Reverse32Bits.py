# -*- coding: utf-8 -*-
"""BitManipulation__Reverse32Bits.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GzX041QNc4DjGfXxyrVJ1KthFsBueseM

Reverse Bits.

Given a 32 bit number X, reverse its binary and print output in decimal.

Example 1:

*INPUT:*

1

*OUTPUT:*

214783648

Example 2:

*INPUT:*

5

*OUTPUT:*

2684354560
"""

def rev_32bits(N):
  num=[]
  while (N>0):
    x=N%2
    num.append(x)
    N=N//2
  while (len(num)<32):
    num.append(0)
  bin_dec(num)

def bin_dec(num):
  value=0
  x=len(num)-1
  for i in range(len(num)):
    value=value+(2**x)*num[i]
    x-=1
  print(value)

print("Enter the integers: ")
x=int(input())
rev_32bits(x)