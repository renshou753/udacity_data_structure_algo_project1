
class Node(object):
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        node = self.cache.get(key)
        if node is None:
            return -1
        else:
            self.shuffle_order(node)
            return node.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        node = self.cache.get(key)
        if node is not None:
            node.value = value
            self.shuffle_order(node)
        else:
            if len(self.cache) >= self.capacity:
                key_remove = self.removeLRU()
                self.cache.pop(key_remove)

            new_node = Node(key, value)
            self.cache[key] = new_node
            self.add_node(new_node)

    def removeLRU(self):
        return self.delete_node(self.head)

    def shuffle_order(self, node):
        if node == self.tail:
            # if node is at the tail, do nothing
            return

        self.delete_node(node)
        self.add_node(node)

    def add_node(self, node):
        if self.tail is not None:
            self.tail.next = node
            node.pre = self.tail
            node.next = None

        self.tail = node
        if self.head is None:
            self.head = node

    def delete_node(self, node):
        if node == self.head and node == self.tail:
            # delete the only element
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            self.head.pre = None
        elif node == self.tail:
            self.tail = self.tail.pre
            self.tail.next = None
        else:
            # delete middle node
            node.pre.next = node.next
            node.next.pre = node.pre

        return node.key


    def ppprint(self):
        node = self.head
        result = []
        while node:
            pair = {node.key:node.value}
            result.append(pair)

            node = node.next

        print(result)

def test_function():
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    print ("Pass" if (our_cache.get(1) == 1) else "Fail")
    print ("Pass" if (our_cache.get(2) == 2) else "Fail")
    print ("Pass" if (our_cache.get(9) == -1) else "Fail")

    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    our_cache.ppprint()

    print ("Pass" if (our_cache.get(3) == -1) else "Fail") # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    our_cache.ppprint()


if __name__ == '__main__':
    test_function()

