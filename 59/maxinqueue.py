from collections import deque


class QueueWithMax():
    def __init__(self):
        self.data = deque()
        self.max = deque()
        self.curIndex = 0

    def push(self, value):
        while len(self.max) != 0 and self.data[-1][1] < value:
            self.max.pop()
        self.max.append((self.curIndex, value))
        self.data.append((self.curIndex, value))
        self.curIndex += 1
    
    def pop(self):
        index, v = self.data.popleft()
        if len(self.max) != 0 and index == self.max[0][0]:
            self.max.popleft()
        
    def max(self):
        self.max[0][1]