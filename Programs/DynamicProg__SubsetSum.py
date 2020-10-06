# -*- coding: utf-8 -*-
"""DynamicProg__SubsetSum.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12qLoGbGeZI0chicFmLM6E8iwzdYFD6Wd

Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
Example:

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9

Output: True  

There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30

Output: False

There is no subset that add up to 30.
"""

def subset(wt,W,n):
  t=[[-1 for x in range(W + 1)] for x in range(n + 1)]
  for i in range(n+1):
    for j in range(W+1):
      if i==0:
        t[i][j]=False
      if j==0:
        t[i][j]=True
  for i in range(1,n+1):
    for j in range(1,W+1):
      if wt[i-1]<=j:
        t[i][j]= t[i-1][j-wt[i-1]] or t[i-1][j]
      else:
        t[i][j]= t[i-1][j]
  print(t[n][W])

def subset_recursion(wt,W,n):
  if W==0:
    return True
  if n==0 and W!=0:
    return False
  if wt[n-1]<=W:
    return (subset_recursion(wt,W-wt[n-1],n-1)) or subset_recursion(wt,W,n-1)
  else:
    return subset_recursion(wt,W,n-1)

def subset_memoization(wt,W,n):
  global t
  if W==0:
    return 0
  if n==0 and W!=0:
    return 1
  if t[n][W]!=0:
    return t[n][W]
  if wt[n-1]<=W:
    if (subset_memoization(wt,W-wt[n-1],n-1)==0) or (subset_memoization(wt,W,n-1)==0):
      t[n][W]=0
      return t[n][W]
  else:
    t[n][W]=subset_memoization(wt,W,n-1)
    return t[n][W]

arr=[2,3,7,8,10]
n=len(arr)
sum=11
print(subset(arr,sum,n))
print(subset_recursion(arr,sum,n))
t=[[-1 for i in range(sum + 1)] for j in range(n + 1)] 
print(subset_memoization(arr,sum,n))