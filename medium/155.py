# Minimum Stack
# Design a stack class that supports the push, pop, top, and getMin operations.

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in O(1) time.


class MinStack:

    def __init__(self):
        self.item = []

    def push(self, val: int) -> None:
        self.item.append(val)

    def pop(self) -> None:
        self.item.pop()

    def top(self) -> int:
        return self.item[len(self.item) - 1]

    def getMin(self) -> int:
        return min(self.item)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
