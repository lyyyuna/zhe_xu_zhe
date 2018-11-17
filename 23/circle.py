class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def findLoop(pHead):
    p1 = pHead
    p2 = pHead

    while True:
        for _ in range(2):
            p1 = p1.next
            if p1 is None:
                return False, None
        p2 = p2.next

        if p1 == p2:
            break

    cnt = 0
    while True:
        cnt +=1 
        p1 = p1.next
        if p1 == p2:
            return True, cnt


def findEntry(pHead):
    isExist, length = findLoop(pHead)
    if isExist == False:
        return None

    p1 = pHead
    p2 = pHead
    for _ in range(length):
        p1 = p1.next
    
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1


l1_6 = Node(6)
l1_5 = Node(5, l1_6)
l1_4 = Node(4, l1_5)
l1_3 = Node(3, l1_4)
l1_2 = Node(2, l1_3)
l1_1 = Node(1, l1_2)
l1_6.next = l1_5
head = l1_1
print findEntry(head).value