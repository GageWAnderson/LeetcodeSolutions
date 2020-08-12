class MinStack: #maintain another stack with the stack tracking the minimum for each unique stack
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minima = [inf]
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if(x < self.minima[-1]):
            self.minima.append(x)
        else:
            self.minima.append(self.minima[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minima.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minima[-1]


#NOTE: You can also use a doubly-linked list to keep track of the minimum in each node
#(After all, stacks are linked-lists)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()