class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            mini = self.stack[-1][1]
            self.stack.append((val,min(val,mini)))
        else: self.stack.append((val,val))

    def pop(self) -> None:
        val,_ = self.stack.pop()
        return val

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
