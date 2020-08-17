# -*- coding: utf-8 -*-
"""LinkedList__DetectLoop_FindStart_CountNode_Remove.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zq_KxWsMXllB4LygGqkkcw2QLL9y1bye
"""
# FLOYD'S ALGORITHM
class Node:
  def __init__(self,data):
    self.data=data
    self.reference=None
class LinkedList:
  def __init__(self):
    self.head=None
  def insert_end(self,new_data):
    print("---------------------INSERTING NODE--------------------")
    new_node=Node(new_data)
    presentNode=self.head
    if (presentNone==None):
      self.head=new_node
    else:
      while (presentNone.reference):
        presentNode=presentNone.reference
      presentNone.reference=new_node
  def traverse(self):
    print("---------------------TRAVERSING--------------------")
    presentNode=self.head
    if (presentNode==None):
      print("Linked List is empty")
      return
    else:
      while (presentNode):
        print(presentNode.data)
        presentNode=presentNode.reference
  def countNode_loop(self):
    first=self.head
    second=self.head
    #detect loop
    print("---------------------DETECTING LOOP--------------------")
    while (first and second and second.reference!=None):
      first=first.reference
      second=second.reference.reference
      if first==second:
        print("There is a loop")
        LL.find_start(first)
        return
    print("No loop")
  def find_start(self,first):
    #Find the start of loop
    print("---------------------FINDING START OF THE LOOP--------------------")
    presentNode=self.head
    while (presentNode!=first):
      presentNode=presentNode.reference
      first=first.reference
    LL.count_nodes(presentNode,first)
  def count_nodes(self,presentNode,first):
    print("---------------------COUNTING NODES IN LOOP--------------------")
    count=1
    #Both presentNode and first points to the start of loop
    #Count the number of nodes now.
    while presentNode.reference!=first:
      presentNode=presentNode.reference
      count+=1
    print(count)
  def removeLoop(self):
    print("---------------------REMOVING THE LOOP--------------------")
    first=self.head
    second=self.head
    #detect loop
    while (first and second and second.reference!=None):
      first=first.reference
      second=second.reference.reference
      if first==second:
        LL.find_second_start(first)
        return
    print("No loop")
  def find_second_start(self,first):
    #Find the start of loop
    presentNode=self.head
    while (presentNode.reference!=first.reference):
      presentNode=presentNode.reference
      first=first.reference
    presentNode.reference=None
    LL.traverse()

LL=LinkedList()
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
LL.head=n1
n1.reference=n2
n2.reference=n3
n3.reference=n4
n4.reference=n5
LL.traverse()
n5.reference=n2
LL.countNode_loop()

LL.removeLoop()
