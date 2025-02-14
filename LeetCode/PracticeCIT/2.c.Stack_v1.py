"""
IMPLEMENTATION USING ARRAY
"""
stack = []

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

print("Stack:", stack)  # Output: [1, 2, 3]

# Pop elements from the stack
top = stack.pop()
print("Popped:", top)   # Output: 3
print("Stack after pop:", stack)  # Output: [1, 2]

stack = [10, 20, 30]
top_element = stack[-1]  # Peek top element
print(top_element)  # Output: 30
print(stack)  # Output: [10, 20, 30] (unchanged)

stack = []
print(len(stack) == 0)  # Output: True

stack.append(10)
print(len(stack) == 0)  # Output: False


"""
IMPLEMENTATION USING DEQUE
"""

from collections import deque

stack = deque()

# Push elements
stack.append(1)
stack.append(2)
stack.append(3)

print("Stack:", stack)  # Output: deque([1, 2, 3])

# Pop elements
print("Popped:", stack.pop())  # Output: 3
print("Stack after pop:", stack)  # Output: deque([1, 2])
