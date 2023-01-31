class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def search(self, data):
        node = self.head

        while node:
            if node.value == data:
                return node

            node = node.next

        return None

def union(llist_1, llist_2):
    # Your Solution Here
    ll = LinkedList()

    node = llist_1.head
    while node:
        s = ll.search(node.value)
        if s is None:
            ll.append(node.value)

        node = node.next

    node = llist_2.head
    while node:
        s = ll.search(node.value)
        if s is None:
            ll.append(node.value)

        node = node.next

    return ll

def intersection(llist_1, llist_2):
    # Your Solution Here
    ll = LinkedList()

    node = llist_1.head
    while node:
        t1 = llist_2.search(node.value)
        t2 = ll.search(node.value)
        if t1 and t2 is None:
            ll.append(node.value)

        node = node.next

    return ll

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [5, 8, 4, 6]
element_2 = [5, 10000, 2, 3]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Test Case 2
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [0]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7,linked_list_8))
print (intersection(linked_list_7,linked_list_8))

# Test Case 3
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = [1, 2, 3, 4, 5, 6]
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print (union(linked_list_9,linked_list_10))
print (intersection(linked_list_9,linked_list_10))

