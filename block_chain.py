
import hashlib

import time

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

class BlockChain(object):
    def __init__(self):
        self.__size = 0
        self.head = None

    def add(self, data):

        if self.head is None:
            block = Block(time.time(), data, None)
            self.head = block
        else:
            block = Block(time.time(), data, self.head)
            self.head = block

        self.__size += 1

    def to_list(self):
        result = []

        node = self.head
        while node:
            result.append(node.data)
            node = node.previous_hash

        return result

    def size(self):
        return self.__size

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node

            node = node.previous_hash

        return None

if __name__ == "__main__":
    blockchain = BlockChain()

    blockchain.add('awesome tony')
    print("Pass" if blockchain.size() == 1 else "Fail")
    print("Pass" if blockchain.to_list() == ['awesome tony'] else "Fail")

    blockchain.add('balance: 200')
    print("Pass" if blockchain.size() == 2 else "Fail")
    print("Pass" if blockchain.to_list() == ['balance: 200', 'awesome tony'] else "Fail")

    print("Pass" if blockchain.search("awesome tony") != None else "Fail")
    print("Pass" if blockchain.search("bad tony") == None else "Fail")
