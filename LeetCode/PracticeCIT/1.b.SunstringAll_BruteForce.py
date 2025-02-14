"""
FINDING ALL THE SUBSTRING OF A GIVEN LENGTH - BRUTE FORCE
"""
def fixed_length_substrings(s, k):
    substrings = []
    print(len(s) - k + 1)
    for i in range(len(s) - k + 1):
        print(len(s) - k + 1)
        print(i,i+k)
        substrings.append(s[i:i + k])
    return substrings

s = "abcdef"
k = 3
print(fixed_length_substrings(s, k))