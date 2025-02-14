"""
FINDING ALL THE SUBSTRING - BRUTE FORCE
"""
def all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i,len(s)):
            substrings.append(s[i:j+1])
            print(substrings)
    
    return substrings

s = "abc"
print(all_substrings(s))