

# Easy

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"

# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"

# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"

 

# Constraints:

#     1 <= num1.length, num2.length <= 104
#     num1 and num2 consist of only digits.
#     num1 and num2 don't have any leading zeros except for the zero itself.

def addStrings(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    # return str(int(num1)+int(num2))
    n1 = num1[::-1]
    n2 = num2[::-1]
    i = 0
    j=0
    cy=0
    res = []
    while i<len(n1) or j<len(n2) or cy:
        d1= int(n1[i]) if i < len(n1) else 0
        d2 = int(n2[j]) if j < len(n2) else 0
        
        d = d1+d2+cy

        r = d%10
        cy = d//10

        res.append(str(r))
        i+=1
        j+=1
    return str(''.join(res[::-1]))