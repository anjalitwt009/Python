

# EASY

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

 

# Constraints:

#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lowercase English letters if it is non-empty.

def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""

    prefix = ""
    for i in range(len(strs[0])):  # loop through each character in the first string
        for j in range(1, len(strs)):  # compare with every other string
            # Check if index i is out of range or characters mismatch
            if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                return prefix
        prefix += strs[0][i]  # all strings matched this character, add to prefix

    return prefix