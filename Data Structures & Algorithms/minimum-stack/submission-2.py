class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.stack is None:
            self.stack.append(val)
            self.min_stack.append(val)
        else:
            self.stack.append(val)
            val = min(val, self.min_stack[-1] if self.min_stack else val)
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
    
        self.stack.pop()
        self.min_stack.pop()
            

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
