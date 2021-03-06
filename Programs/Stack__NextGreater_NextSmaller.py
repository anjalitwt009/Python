# -*- coding: utf-8 -*-
"""Stack__NextGreater_NextSmaller.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U6FbjQqZbxySFGkGMZIQ2rqKDYxr0AAj

Question 1:

Next Larger element.

Given an array A of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array. If no such element exists, output -1 

Input:
The first line of input contains a single integer T denoting the number of test cases.Then T test cases follow. Each test case consists of two lines. The first line contains an integer N denoting the size of the array. The Second line of each test case contains N space separated positive integers denoting the values/elements in the array A.

Output:
For each test case, print in a new line, the next greater element for each array element separated by space in order.

Example 1:

*INPUT:*

1,3,2,4

*OUTPUT:*

3,4,4,-1

Example 2:

*INPUT:*

1,2,3,4

*OUTPUT:*

-1,-1,-1,-1

Question 2:

Immediate Smaller Element.

Given an integer array of size N. For each element in the array, check whether the right adjacent element (on the next immediate position) of the array is smaller. If next element is smaller, print that element. If not, then print -1.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains 2 lines of input:
The first line contains an integer N, where N is the size of array.
The second line contains N integers(elements of the array) sperated with spaces.

Output:
For each test case, print the next immediate smaller elements for each element in the array.

Example 1:

*INPUT:*

4,2,1,5,3

*OUTPUT:*

2,1,-1,3,-1

Example 2:

*INPUT:*

5,6,2,3,1,7

*OUTPUT:*

-1,2,-1,1,-1,-1
"""

class Stack:
  def __init__(self,n):
    self.stack=[]
    self.size=n

  def push(self,element):
    if (len(self.stack) == self.size):
      print("STACK IS FULL")
    else:
      self.stack.append(element)

  def pop(self):
    if (len(self.stack) == 0):  #or self.stack==[]
      print("STACK IS EMPTY")
      return -1
    else:
      return self.stack.pop()
  
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
      return self.stack[len(self.stack)-1]
    else:
      return -1

def NextLarger(A):
  out_arr=[]
  s=Stack(len(A))
  for i in range(len(A)-1,-1,-1):
    if s.size_stack()==0:
      out_arr.append(-1)
    elif s.size_stack()>0 and s.top()>A[i]:
      out_arr.append(s.top())
    elif s.size_stack()>0 and s.top()<A[i]:
      while (s.size_stack()>0 and s.top()<A[i]):
        s.pop()
        if s.pop()==-1:
          break
      if s.size_stack()==0:
        out_arr.append(-1)
      else:
        out_arr.append(s.top())
    s.push(A[i])
  out_arr.reverse()
  print(out_arr)

def NextSmaller(A):
  out_arr=[]
  s=Stack(len(A))
  for i in range(len(A)-1,-1,-1):
    if s.size_stack()==0:
      out_arr.append(-1)
    elif s.size_stack()>0 and s.top()<A[i]:
      out_arr.append(s.top())
    elif s.size_stack()>0 and s.top()>A[i]:
      while (s.size_stack()>0 and s.top()>A[i]):
        s.pop()
        if s.pop()==-1:
          break
      if s.size==0:
        out_arr.append(-1)
      else:
        out_arr.append(s.top())
    s.push(A[i])
  out_arr.reverse()
  print(out_arr)

#Checking stack functions
A=Stack(3)
A.push(6)
A.push(2)
print(A.stack)
A.pop()
print(A.stack)
print(A.size)
A.isempty()

A=[1,3,0,0,2,4]
NextLarger(A)
NextSmaller(A)
