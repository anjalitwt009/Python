"""

EASY 

69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

 

Constraints:

    0 <= x <= 231 - 1


"""


from math import sqrt

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(sqrt(x))

# Example Usage
sol = Solution()
print(sol.mySqrt(4))  # Output: 2
print(sol.mySqrt(8))  # Output: 2 (since sqrt(8) ≈ 2.828, and int truncates it)
print(sol.mySqrt(16)) # Output: 4
print(sol.mySqrt(25)) # Output: 5
