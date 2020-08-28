# -*- coding: utf-8 -*-
"""ValidateIP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dCLAAypE_NzIKGANX-_Ye4-BfOaWkmDS

Check for valid IPv4 of the format: (0-255).(0-255).(0-255).(0-255). It can contain any number of leading additional zeros.

Example 1:

*INPUT*:

222.111.111.111

*OUTPUT:*

1

Example 2:

*INPUT*:

5555..55

*OUTPUT:*

0

Example 3:

*INPUT*:

0000.0000.0000.0000

*OUTPUT:*

0

Example 1:

*INPUT*:

1.2.3.04

*OUTPUT:*

0
"""

def check_ip(A):
  #1.there has to be at max 3 stops
  #2.since we are reversing string: valid ip range will be from 0 to 552
  #3.between each stop there should be at max 3 digits or length of string should be 3 max
  #4.we need the index of digit after stop
  #5. since it can have any number of leading zeros we need a condition for that too.
  # reversing the ip will have trailing zeros(here)
  
  s=A[::-1]
  initial=0
  stops=0
  for i in range(len(A)):
    if s[i]=='.' and stops<3:
      stops+=1
      #print(int(s[initial:i]))
      if (not ((0<=int(s[initial:i])<=552) and len(s[initial:i])<=3)):  #condition 3,2
        print("Invalid")
        return
      initial=i+1 #condition 4
    if s[initial]=='.' or (s[i]=='.' and stops==3): #condition 1
      print("Invalid")
      return
  num=int(s[initial:len(A)])
  while (num%10==0): #condition 5
    num=num/10
  if 0<=num<=552:
    print("Valid IPv4")
  else:
    print("Invalid")

A=input("Enter the IPv4:")
check_ip(A)