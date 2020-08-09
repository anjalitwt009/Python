# -*- coding: utf-8 -*-
"""LinkedList__IntersectionPoint_'y'shapedLL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pr5ELhcetuJ6G6TEwmaoJSTgW_lt8vg0
"""

class Node:
  def __init__(self,data):
    self.data=data
    self.reference=None

class LinkedList:
  def __init__(self):
    self.head=None

  def find_intersection(self,L1,L2):
    presentNode1=L1.head
    presentNode2=L2.head
    c=-1
    while (presentNode1):
      presentNode2=L2.head
      while (presentNode2):
        if presentNode1.data==presentNode2.data:
          print(presentNode1.data)
          return
        presentNode2=presentNode2.reference
      presentNode1=presentNode1.reference
    print(c)
    return
  def insert_end(self,data):
    presentNode=self.head
    new_node=Node(data)
    if (presentNode==None):
      self.head=new_node
      return
    while (presentNode.reference):
      presentNode=presentNode.reference
    presentNode.reference=new_node
  def insert_common_ele(self,data,L2):
    new_node=Node(data)
    presentNode1=self.head
    presentNode2=L2.head
    if (presentNode1==None):
      self.head=new_node
    else:
     while (presentNode1.reference):
       presentNode1=presentNode1.reference
    presentNode1.reference=new_node
    if (presentNode1==None):
      L2.head=new_node
    else:
      while (presentNode2.reference):
        presentNode2=presentNode2.reference
      presentNode2.reference=new_node
  def traverse(self):
    presentNode=self.head
    while (presentNode):
      print(presentNode.data)
      presentNode=presentNode.reference

print("Enter the size of 1st linked list:")
N=int(input())
print("Enter the size of 2nd linked list:")
M=int(input())

n1=Node(1)
n2=Node(2)
n3=Node(3)
inter_node=Node(10)
n4=Node(4)
n5=Node(5)

n6=Node(6)
n7=Node(7)
L1=LinkedList()
L2=LinkedList()
L1.head=n1
n1.reference=n2
n2.reference=n3
n3.reference=inter_node
inter_node.reference=n4
n4.reference=n5
L1.traverse()

L2.head=n4
n4.reference=inter_node
inter_node.reference=n5
L2.traverse()

L1.find_intersection(L1,L2)