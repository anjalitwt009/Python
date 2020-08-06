# -*- coding: utf-8 -*-
"""Strings__CountAnagrams.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ksybRe6D2JUP1NBpOi92izAzGW-ubkx5

Count Anagrams.

Given a word S and a text C. Return the count of anagrams of the word in text.

Example 1:

*INPUT:*

S=forxxorfxdofr

C=for

*OUTPUT:*

3

Example 2:

*INPUT:*

S=aabaabaa

*OUTPUT:*

4
"""

def check_anagram(S,C):
  D1={}
  for ele in C:
    try:
      D1[ele]+=1
    except:
      D1[ele]=1
  print(D1)
  D2={}
  count_ana=0

  for ele in range(len(S)-len(C)+1):
    D2=D1.copy()
    i=0
    c=0
    #print("ele",ele)
    while (i<len(C)):
      #print("The element,i is(1): ",S[i+ele],i)
      #print("The dict_element,i is(1): ",D2[S[i+ele]],i)
      if S[i+ele] in D2.keys() and D2[S[i+ele]]>0:
        D2[S[i+ele]]-=1
        c+=1
        #print("The element,i is: ",S[i+ele],i)
      i+=1
    if c==len(C):
      count_ana+=1
  print(count_ana)

S=input("Enter the first string: ")
C=input("Enter the second string: ")
check_anagram(S,C)