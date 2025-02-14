"""
647. PALINDROMIC SUBSTRING

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

 

Constraints:

    1 <= s.length <= 1000
    s consists of lowercase English letters.


"""

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss1 = self.substring(s)
        count = 0
        for i in range(len(ss1)):
            if self.palindrome(ss1[i]):
                count += 1
        return count

    def substring(self, s, start=0, substrings=None):
        if start == len(s):
            return substrings  # Return the list when done

        if substrings is None:
            substrings = []

        for i in range(start + 1, len(s) + 1):
            substrings.append(s[start:i])
        
        return self.substring(s, start + 1, substrings)  # Corrected recursive call -- DONT USE START = START+1

    def palindrome(self, ss):
        return ss == ss[::-1]

sol = Solution()
s = "aaa"
print(sol.countSubstrings(s))  # Output: 6



##################
"""
ALTERNATE SOLUTION
"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        c, ss1 = self.substring(s)
        return c

    def substring(self, s,  c = 0, start = 0, substrings=None):
        if start == len(s):
            return c, substrings  # Return the list when done

        if substrings is None:
            substrings = []

        for i in range(start + 1, len(s) + 1):
            if self.palindrome(s[start:i]):
                c += 1
            substrings.append(s[start:i])
        
        return self.substring(s, c , start + 1, substrings)  # Corrected recursive call

    def palindrome(self, ss):
        return ss == ss[::-1]

#################

"""

IDEAL CODE: O(n^2)

"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        
        def expandAroundCenter(left, right):
            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            expandAroundCenter(i, i)     # Odd-length palindromes
            expandAroundCenter(i, i + 1) # Even-length palindromes

        return count

sol = Solution()
print(sol.countSubstrings("abc"))  # Output: 3
print(sol.countSubstrings("aaa"))  # Output: 6