# 
# EASY
# 
# 
# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

# Given an integer n, return a list of two integers [a, b] where:

#     a and b are No-Zero integers.
#     a + b = n

# The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

 

# Example 1:

# Input: n = 2
# Output: [1,1]
# Explanation: Let a = 1 and b = 1.
# Both a and b are no-zero integers, and a + b = 2 = n.

# Example 2:

# Input: n = 11
# Output: [2,9]
# Explanation: Let a = 2 and b = 9.
# Both a and b are no-zero integers, and a + b = 11 = n.
# Note that there are other valid answers as [8, 3] that can be accepted.

 

# Constraints:

#     2 <= n <= 104
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def not_zero(x):
    return ('0' not in str(x))

def get_no_zero_int(n):
    for a in range(n):
        b= n-a
        if not_zero(a) and not_zero(b):
            return [a,b]
        
print(get_no_zero_int(5))


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def get_no_zero_int(n):
    for i in range(1,n):
        if "0" not in (str(n-i)) and "0" not in str(i):
            return [i,n-i]
        
print(get_no_zero_int(5))