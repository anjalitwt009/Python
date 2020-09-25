# -*- coding: utf-8 -*-
"""Recursion__DeleteMidEle_Stack.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jw0wIyQdir5xUyBddHJW5oECtrKHqdH7

Given a stack with push(), pop(), empty() operations, delete the middle of it without using any additional data structure.
Middle: ceil(size_of_stack/2.0)
 

Example 1:

Input: 

5

1 2 3 4 5

Output:

1 2 4 5

Explanation:

As the number of elements is 5 , 
hence the middle element will be the 3rd
element which is deleted

Example 2:

Input:

4

1 2 3 4

Output:

1 3 4

Explanation:

As the number of elements is 4 , 
hence the middle element will be the 2nd
â€‹element which is deleted
 

Your Task:

This is a function problem. The input is already taken by the driver code. You only need to complete the function deleteMid() which takes 3 arguments(stack, size of the stack, and current index - initially 0) and returns the modified stack.

Expected Time Complexity: O(N).

Expected Auxiliary Space: O(1).

Constraints:

1 <= sizeOfStack <= 100
"""

class Stack:
  def __init__(self,n):
    self.stack=[]
    self.size=n

  def push(self,element):
    if (len(self.stack) == self.size):
      printf("STACK IS FULL")
    else:
      self.stack.append(element)

  def pop(self):
    if (len(self.stack) == 0):  #or self.stack==[]
      printf("STACK IS EMPTY")
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

def delmid(s):
  if s.size_stack()==0:
    return s
  x=s.size_stack()
  k=(x//2)+1
  solve(s,k)

def solve(s,k):
  if k==1:
    s.pop()
    return s
  temp=s.top()
  s.pop()
  solve(s,k-1)
  s.push(temp)
  return s

s=Stack(6)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
delmid(s)
print("------")
print(s.top())
s.pop()
print(s.top())
s.pop()
print(s.top())
s.pop()
print(s.top())
s.pop()
print(s.top())
s.pop()
print("------")