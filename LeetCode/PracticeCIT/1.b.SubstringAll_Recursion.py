"""
FINDING ALL THE SUBSTRING OF A GIVEN LENGTH - RECURSION
"""
def get_substrings(s, start=0, substrings=None):
    if substrings is None:
        substrings = []
    if start == len(s):
        return substrings
    for i in range(start + 1, len(s)+1):
        substrings.append(s[start:i])
    return get_substrings(s, start + 1, substrings)

s = "abc"
print(get_substrings(s))