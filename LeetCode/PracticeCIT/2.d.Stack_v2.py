class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, item):
        """Push an item onto the stack."""
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Pop the top item from the stack and return it."""
        if not self.is_empty():
            popped_item = self.stack.pop()
            print(f"Popped: {popped_item}")
            return popped_item
        print("Stack is empty, cannot pop.")
        return None

    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        print("Stack is empty.")
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)

    def insert_at_bottom(self, item):
        """Insert an item at the bottom of the stack."""
        if self.is_empty():
            self.push(item)
        else:
            temp = self.pop()
            self.insert_at_bottom(item)
            self.push(temp)

    def display(self):
        """Display the stack elements."""
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):", self.stack[::-1])


# 🔹 **Usage Example**
s = Stack()

# Pushing elements
s.push(10)
s.push(20)
s.push(30)

# Display stack
s.display()

# Peek top element
print("Top element:", s.peek())

# Pop elements
s.pop()
s.display()

# Insert at bottom
s.insert_at_bottom(5)
s.display()

# Stack size
print("Stack size:", s.size())

# Check if stack is empty
print("Is stack empty?", s.is_empty())
