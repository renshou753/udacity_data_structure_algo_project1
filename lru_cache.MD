#### Code Design

I used hash map and doubly linked list for this particular problem. Hash map is a perfect choice for caching due to its fast read/write time complexity of O(1).

Doubly linked list was used mainly because I need to preserve the orders of the cache, hash map itself does not have orders for its individual nodes so I have to use doubly linked list to maintain the orders for both previous node and next node so when user tries to retrieve the element from the hashmap I could re-shuffle the orders of the cache in order to remove the infrequently accessed node if necessary.

#### Efficiency

Similar to hashmap, only to get the element from the LRU cacheh or set element has time complexity of O(1); Getting or setting element for the LRU cache requires re-shuffling the program which also has time complexity of O(1) because in the program we linked previous node and next node for each node in doubly linked list, i.e. loop is not required to delete a node from the middle of the list or add a node to the tail, so on average O(1) time complexity.

In terms of space it can be heavy, the program requires two data structure: one linked list of O(n), and a hashmap taking at least O(n) as well depends on the implementation of the hash functions. On average space complexity should be O(n).
