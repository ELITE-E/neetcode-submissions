class MinStack:

    def __init__(self):
       self.stack = []
       self.minStack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val ,self.minStack[-1] if self.minStack else val)
        
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# So, the question is really asking: How can you always instantly know the minimum element currently in the stack, no matter how many items are pushed or popped, without ever having to search for it?