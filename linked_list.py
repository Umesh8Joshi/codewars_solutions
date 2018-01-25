# program to merge two linked list

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def merge(L1,L2):

    L3 = Node(None, None)
    prev = L3

    while L1 != None and L2 != None:
        if L1.data <= L2.data:
            prev.next = L2.data
            L1 = L1.next
        else:
            prev.data = L1.data
            L2 = L2.next
        prev = prev.next

    if L1.data == None:
        prev.next = L2
    elif L2.data == None:
        prev.next  = L1

    return L3.next

if __name__ == '__main__':
    n3 = Node(10, None)
    n2 = Node(n3, 7)
    n1 = Node(n2, 5)
    L1 = n1

    n7 = Node(12, None)
    n6 = Node(n7, 9)
    n5 = Node(n6, 6)
    n4 = Node(n5, 2)
    L2 = n4

    merged = merge(L1, L2)
    while merged != None:
        print(str(merged.data) + '->')
        merged = merged.next
    print('None')