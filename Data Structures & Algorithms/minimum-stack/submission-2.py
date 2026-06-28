class MinStack:
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        old_min = val if self.min is None else self.min
        if val <= old_min:
            self.stack.append(2 * val - old_min)
            self.min = val
        else:
            self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped <= self.min:
            self.min = 2 * self.min - popped
        if not self.stack:
            self.min = None

    def top(self) -> int:
        return max(self.min, self.stack[-1])

    def getMin(self) -> int:
        return self.min
