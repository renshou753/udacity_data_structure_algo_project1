
import sys

huffman_dic = {}

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
 
    def __str__(self):
        return ' '.join([f"{i.key}:{i.value}" for i in self.queue])

    def size(self):
        return len(self.queue)
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def insert(self, node):
        self.queue.append(node)

    # pop out element that has highest priority(lowest frequency)
    def pop(self):
        priority_index = 0
        for i in range(len(self.queue)):
            if self.queue[i].value < self.queue[priority_index].value:
                priority_index = i

        item = self.queue[priority_index]
        del self.queue[priority_index]
        return item

class Node(object):
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self._left = left
        self._right = right

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def has_left(self):
        return True if self._left is not None else False

    def has_right(self):
        return True if self._right is not None else False

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node

def depth_pre_order(node, binary_code, direction):
    if node is None:
        return

    if direction == 'left':
        binary_code += '0'
    elif direction == 'right':
        binary_code += '1'

    if node.key:
        huffman_dic[node.key] = binary_code

    depth_pre_order(node.get_left(), binary_code, "left")
    depth_pre_order(node.get_right(), binary_code, "right")

def huffman_encoding(data):

    dic = get_char_frequency(data)
    queue = PriorityQueue()
    for k, v in dic.items():
        node = Node(k, v)
        queue.insert(node)

    while queue.size() >= 2:
        # remove two minimum elements from the priority queue
        item_1 = queue.pop()
        item_2 = queue.pop()

        # merge two nodes to create a new node, reinsert the new node into priority queue
        node = Node("", item_1.value + item_2.value, item_1, item_2)
        queue.insert(node)

    tree = queue.queue[0]
    depth_pre_order(tree, '', '')

    encoding = ""

    for char in data.lower():
        encoding += huffman_dic[char]

    return encoding, tree

def huffman_decoding(data,tree):
    str_to_decode = ""
    decoded_data = ""
    for s in data:
        str_to_decode += s
        for k,v in huffman_dic.items():
            if str_to_decode == v:
                decoded_data += k
                str_to_decode = ""
                break

    return decoded_data

def get_char_frequency(s:str) -> dict:
    dic = {}

    for key in s.lower():
        dic[key] = dic.get(key, 0) + 1

    return dict(sorted(dic.items(), key=lambda item: item[1]))

if __name__ == "__main__":

    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    # Add your own test cases: include at least three test cases
    # and two of them must include edge cases, such as null, empty or very large values

    # Test Case 1
    # reset huffman dic
    huffman_dic = {}

    a_great_sentence = "There is a nice bird on sky"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    print("Pass" if len(a_great_sentence) == len(decoded_data) else "Fail")

    # Test Case 2
    huffman_dic = {}

    a_great_sentence = "1289371238968y128937128903709127390703ik12uj3kl12il3u12893712io3uio12u3io"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    print("Pass" if len(a_great_sentence) == len(decoded_data) else "Fail")

    # Test Case 3
    huffman_dic = {}

    a_great_sentence = "abc"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    print("Pass" if len(a_great_sentence) == len(decoded_data) else "Fail")

