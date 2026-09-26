class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if value < self.min:
            self.min = value

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        item = self.stack.pop()
        if item == self.min:
            self.min = min(self.stack) if self.stack else float('inf')
        

    def top(self) -> int:
        if len(self.stack) == 0:
            return 0
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min