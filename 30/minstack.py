class MinStack():
    def __init__(self):
        self.real_stack = []
        self.min_stack = []

    def push(self, num):
        self.real_stack.append(num)

        if not self.min_stack:
            self.min_stack.append(num)
        else:
            min_now = self.min_stack[-1]
            if num < min_now:
                self.min_stack.append(num)
            else:
                self.min_stack.append(min_now)

    def pop(self):
        if not self.min_stack or not self.real_stack:
            return None

        self.min_stack.pop()
        return self.real_stack.pop()

    def min(self):
        if not self.min_stack:
            return None

        return self.min_stack[-1]


s = MinStack()
s.push(2.98)
s.push(3)
print(s.real_stack)
print(s.min())
s.pop()
print(s.real_stack)
print(s.min())
s.push(1)
print(s.real_stack)
print(s.min())
s.pop()
print(s.real_stack)
print(s.min())