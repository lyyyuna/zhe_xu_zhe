class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_list_reverse(head):
    if head is None:
        return False

    stack = []
    p = head
    while p:
        stack.append(p)
        p = p.next

    while stack != []:
        print stack.pop().data,
    

n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)
print_list_reverse(n1)
    