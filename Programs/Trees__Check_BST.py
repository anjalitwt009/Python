# -*- coding: utf-8 -*-
"""Trees_Check_BST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mVb0YKTxCpUDoGIIYE-5ztscA2Ld3ZqI
"""

class Node:
  def __init__(self,data):
    self.left=None
    self.data=data
    self.right=None

def BST(root):
  if root and root.left and root.right:
    if root.left.data < root.data and root.right.data > root.data:
      return True
    else:
      return bool(BST(root.left and root.right))
  else:
    return

n1=Node(5)
n2=Node(9)
n3=Node(7)
n1.left=n2
n1.right=n3

print(BST(n1))