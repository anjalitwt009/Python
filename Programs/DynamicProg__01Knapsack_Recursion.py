# -*- coding: utf-8 -*-
"""DynamicProg__01KnapSack_Recursion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O-EvCiTHu9kPaYxSyySHJglLlD8XUioL

Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).

INPUT:

val = [60, 100, 120] 

wt = [10, 20, 30] 

W = 50

n = len(val) 

OUTPUT:

220
"""

def knap_01(wt,val,W,n):
  if n==0 or W==0:
    return 0
  if wt[n-1]<=W:
    return max((val[n-1]+knap_01(wt,val,W-wt[n-1],n-1)),
               knap_01(wt,val,W,n-1))
  else:
    return knap_01(wt,val,W,n-1)

val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val)
ans=knap_01(wt,val,W,n)
ans