# -*- coding: utf-8 -*-
"""Recursion__Permutation_CaseChange.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yOyp18bYXKaryhRAn8Pl1sstFm_xgxMF
"""

def permutations(I,O):
  if len(I)==0:
    print(O)
    return
  O1=''
  O2=''
  for i in O:
    O1+=i
    O2+=i
  
  O1+=I[0] 
  O2+=(I[0].upper())
  #print(O2)

  IN=''
  for i in range(1,len(I)):
    IN = IN + I[i]
  permutations(IN,O1)
  permutations(IN,O2)
  return

permutations('ab','')