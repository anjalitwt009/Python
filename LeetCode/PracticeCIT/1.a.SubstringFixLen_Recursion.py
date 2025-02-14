"""
FINDING ALL THE SUBSTRING - RECURSION
"""
def get_fixed_length_substrings(s, k, start=0, substrings=None):
    if substrings is None:
        substrings = []
    if start > len(s) - k:  # Stop when remaining characters are less than k
        return substrings
    substrings.append(s[start:start + k])  # Add substring of length k
    return get_fixed_length_substrings(s, k, start + 1, substrings)  # Move start forward

s = "abcdef"
k = 3
print(get_fixed_length_substrings(s, k))
