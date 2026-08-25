class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoList(a, b):
    dummy = ListNode()
    current = dummy

    while a and b:
        if a.val < b.val:
            current.next = a
            a = a.next
        else:
            current.next = b
            b = b.next
        current = current.next
    
    if a:
        current.next = a
    else:
        current.next = b

    return dummy.next

def mergeThreeList(l1, l2, l3):

    left = mergeTwoList(l1, l2)
    answer = mergeTwoList(left, l3)

    return answer

def createList(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next

def printList(head):
    current = head

    while current:
        print(current.val, end=" --> ")
        current = current.next
    print("None")

l1 = createList([1, 4, 7])
l2 = createList([2, 5, 8])
l3 = createList([3, 6, 9])

print("List 1:")
printList(l1)

print("List 2:")
printList(l2)

print("List 3:")
printList(l3)

answer = mergeThreeList(l1, l2, l3)

print("Merged List:")
printList(answer)
