# -*- coding: utf-8 -*-
"""Strings__NonRepeatingChar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p2g61I6vTJ273RDxT22BVs_BTrSX1AiS
"""

def non_rep(A):
  D={}
  for ele in A:
    try:
      D[ele]+=1
    except:
      D[ele]=1
  for key in D.keys():
    if D[key]==1:
      print(key)
      return

A=input("Enter string: ")
non_rep(A)