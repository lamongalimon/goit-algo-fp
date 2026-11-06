class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None  # link to the next node


class LinkedList:
    def __init__(self):
        self.head = None  # first node; None means the list is empty

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # new node points to the old head
        self.head = new_node       # new node becomes the head

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:            # walk to the last node
            cur = cur.next
        cur.next = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        self.head = prev

def merge(a, b):
    dummy = Node()
    tail = dummy
    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    if b is not None:
        tail.next = b
    else:
        tail.next = a
    
    return dummy.next

def split(head):
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next
    cur = head
    for _ in range(n//2 -1):
        cur = cur.next
    right = cur.next
    cur.next = None

    return head, right

def merge_sort(head):
    if head is None or head.next is None:
        return head
    left, right = split(head)     
    left = merge_sort(left)       
    right = merge_sort(right)     
    return merge(left, right)     


l1 = LinkedList()
for v in [1, 4, 7, 9]:
    l1.insert_at_end(v)
l2 = LinkedList()
for v in [2, 3, 8]:
    l2.insert_at_end(v)

result = LinkedList()
result.head = merge(l1.head, l2.head)
result.print_list()

l3 = LinkedList()
for v in [4, 1, 3, 2]:
    l3.insert_at_end(v)

left_head, right_head = split(l3.head)
left = LinkedList()
left.head = left_head
right = LinkedList()
right.head = right_head
left.print_list()
right.print_list()

l4 = LinkedList()
for v in [4, 1, 3, 9, 12]:
    l4.insert_at_end(v)
l4.head = merge_sort(l4.head)   # sorting may change the head!
l4.print_list()      