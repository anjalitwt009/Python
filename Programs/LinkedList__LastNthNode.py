# -*- coding: utf-8 -*-
"""LinkedList__LastNthNode.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18cD2UZlPbaPxkllUzK2ZoNAaU0b2irjR

Nth node from the end of the linked list.

Example 1:

*INPUT:*

L=9

N=2

Val=1,2,3,4,5,6,7,8,9

*OUTPUT:*

8

Example 2:

*INPUT:*

L=4

N=5

Val=10,5,100,5

*OUTPUT:*

-1
"""

class Node:
  def __init__(self,data):
    self.data=data
    self.reference=None

class LinkedList:
  def __init__(self):
    self.head=None
  
  def insert_end(self,data):
    print("--------INSERTING NODE AT THE END---------")
    presentNode=self.head
    new_data=Node(data)
    if (presentNode==None):
      self.head=new_data
    else:
      while (presentNode.reference!=None):
        presentNode=presentNode.reference
      presentNode.reference=new_data

  def traverse(self):
    presentNode=self.head
    if (presentNode==None):
      print("LL is empty")
    while (presentNode):
      print(presentNode.data)
      presentNode=presentNode.reference
  def last_Nth_node(self,N):
    presentNode=self.head
    count=0
    while (presentNode):
      count+=1
      presentNode=presentNode.reference
    if N>count:
      print(-1)
      return
    else:
      trav=count-N+1
      presentNode=self.head
      for i in range(1,trav):
        presentNode=presentNode.reference
      print(presentNode.data)

LL1=LinkedList()
LL1.head=None
print("Enter the number of nodes: ")
N=int(input())
print("Enter the data for Linked list: ")
for i in range(N):
  LL1.insert_end(int(input()))
print("Entered Linked List is: ")
LL1.traverse()
N=int(input("Enter N: "))

LL1.last_Nth_node(N)