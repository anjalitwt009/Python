# -*- coding: utf-8 -*-
"""Recursion__Letter_Case_Permutation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G8yCu-eYXaOJFTgQdSfjqwYj_BDjE1yD
"""

Out=[]
def Permutations(I,O):
  global Out
  if len(I)==0:
    Out.append(O)
    #set(Out)
    #print(set(Out))
    return 
  O1=''
  O2=''
  for i in O:
    O1+=i
    O2+=i

  if I[0].isalpha:
    O1+=I[0].lower()
    O2+=I[0].upper()
    IN=''
    for i in range(1,len(I)):
      IN = IN + I[i]
    Permutations(IN,O1)
    Permutations(IN,O2)
  else:
    O1+=I[0]
    IN=''
    for i in range(1,len(I)):
      IN = IN + I[i]
    Permutations(IN,O1)
  
  return

Permutations("a1B2"," ")
set(Out)