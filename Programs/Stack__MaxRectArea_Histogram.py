# -*- coding: utf-8 -*-
"""Stack__MaxRectArea_Histogram.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ACo-BATAMqGJg4p8nRnrQ-AE3EAoEu7y

Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit.

Input:

The first line contains an integer 'T' denoting the total number of test cases. T test-cases follow. In each test cases, the first line contains an integer 'N' denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array. The elements of the array represents the height of the bars.

Output:

For each test-case, in a separate line, the maximum rectangular area possible from the contiguous bars.

Constraints:

1 <= T <= 100

1 <= N <= 105

1 <= A[i] <= 104

Example:

Input: 

2

7

6 2 5 4 5 1 6

4

6 3 4 2

Output:

12

9
"""

class Stack:
  def __init__(self,n):
    self.stack=[]
    self.index=[]
    self.size=n

  def push(self,element,index):
    if (len(self.stack) == self.size):
      print("STACK IS FULL")
    else:
      self.stack.append(element)
      self.index.append(index)

  def pop(self):
    if (len(self.stack) == 0):  #or self.stack==[]
      #print("STACK IS EMPTY")
      return -1
    else:
      self.stack.pop()
      self.index.pop()
      return 0
  
  def size_stack(self):
    size=len(self.stack)
    return size

  def isempty(self):
    x=self.size
    if x==0:
      print("Stack is empty")
      return 1
    else:
      print("Not empty")
      return 0

  def top(self):
    if len(self.stack)>0:
      #print (len(self.stack))
      A=[]
      A.append(self.stack[len(self.stack)-1]) 
      A.append(self.index[len(self.stack)-1])
      return A
    else:
      A=[]
      A.append(-1)
      A.append(-1)
      return A

def NSL_index(A):
  out_arr=[]
  out_index=[]
  s=Stack(len(A))
  for i in range(len(A)):
    if s.size_stack()==0:
      out_arr.append(-1)
      out_index.append(-1)
    elif s.size_stack()>0 and s.top()[0]<A[i]:
      out_arr.append(s.top()[0])
      out_index.append(i-1)
    elif s.size_stack()>0 and s.top()[0]>A[i]:
      while (s.size_stack()>0):
        if (s.top()[0]>A[i]):
          s.pop()
          #print(s.size_stack())
        else:
          break
      if s.size_stack()==0:
        out_arr.append(-1)
      else:
        out_arr.append(s.top()[0])
      out_index.append(s.top()[1])
    s.push(A[i],i)
  #out_arr.reverse()
  #print(out_arr)
  print(out_index)
  return out_index

def NSR_index(A):
  out_arr=[]
  out_index=[]
  s=Stack(len(A))
  for i in range(len(A)-1,-1,-1):
    if s.size_stack()==0:
      out_arr.append(0)
      out_index.append(len(A))
    elif s.size_stack()>0 and s.top()[0]<A[i]:
      out_arr.append(s.top()[0])
      out_index.append(i+1)
    elif s.size_stack()>0 and s.top()[0]>A[i]:
      while (s.size_stack()>0):
        if (s.top()[0]>A[i]):
          s.pop()
          #print(s.size_stack())
        else:
          break
      if s.size_stack()==0:
        out_arr.append(0)
        out_index.append(len(A))
      else:
        out_arr.append(s.top()[0])
        out_index.append(s.top()[1])
    s.push(A[i],i)
  out_index.reverse()
  #print(out_arr)
  print(out_index)
  return out_index

def max_ar(A):
  Right=NSR_index(A)
  Left=NSL_index(A)
  width=[]
  max=0
  for i in range(len(A)):
    width.append(Right[i]-Left[i]-1)
    ar=(Right[i]-Left[i]-1)*A[i]
    if ar>max:
      max=ar
  print(width)
  print(max)

A=[6,2,5,4,5,1,6]
max_ar(A)