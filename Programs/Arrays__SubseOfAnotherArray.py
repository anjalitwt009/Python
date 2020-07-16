# -*- coding: utf-8 -*-
"""Arrays__SubsetOfAnotherArray.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y1nXCDz24TcFEb_Swpcyf8xUHwfHYJY4

Find if the given array is a subset of another array. Asuuming arrays can be sorted or unsorted and do not hav any duplicate elements. Also,m>n which are the sizes of the corresponting arrays, Am,An.

*INPUT*:

m=6

Am=[11,1,13,21,3,7]

n=4

An=[11,3,7,1]

*OUTPUT*:

Yes
"""

def array_subset(Am,An,m,n):
  C=[]
  count=0
  for ele in An:
    if ele in Am:
      C.append(ele)
      count=count+1
  if count>0:
    print('Yes')
  else:
    print('No')

if __name__ == "__main__":
  m=int(input())
  print("Enter the larger array elements unsorted order")
  Am=list((input().split(' ')[:m]))
  print(Am)
  n=int(input())
  print("Enter the array elements unsorted order")
  An=list((input().split(' ')[:n]))
  print(An)
  array_subset(Am,An,m,n)