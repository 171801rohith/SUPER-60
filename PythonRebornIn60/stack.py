# Exercise 5: Abstraction with a Stack Class
# Objective: Apply abstraction by implementing a stack with a simple interface.

# Instructions:
# Create a Stack class with a private list __items to store data.

# Implement these methods:
# _init_(self): Initializes an empty stack.
# push(self, item): Adds an item to the top of the stack.
# pop(self): Removes and returns the top item, or raises an IndexError if the stack is empty.
# peek(self): Returns the top item without removing it, or raises an IndexError if empty.
# is_empty(self): Returns True if the stack is empty, False otherwise.

# Write a main function to:
# Create a Stack object.
# Push 1, 2, and 3 onto the stack.
# Print the top item using peek().
# Pop and print each item until the stack is empty.


class Stack:
    def __init__(self):
        self.__items = []
        self.__top = -1

    def push(self, item):
        self.__items.append(item)
        self.__top += 1

    def pop(self):
        if self.__top == -1:
            raise Exception("IndexError if the stack is empty.")

        self.__top -= 1
        return self.__items.pop()

    def peek(self):
        return self.__items[self.__top]

    def display(self):
        print(self.__items)

    def is_empty(self):
        if self.__top == -1:
            return True
        return False


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
print("Peek:", stack.peek())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
