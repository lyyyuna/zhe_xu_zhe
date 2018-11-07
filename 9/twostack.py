class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def append(self, data):
        self.stack1.append(data)

    def popLeft(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


q = Queue()
q.append(1)
q.append(2)
q.append(3)
print q.popLeft()
q.append(4)
print q.popLeft()