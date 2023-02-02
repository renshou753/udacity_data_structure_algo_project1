### Code Design

For encoding a priority queue was used to keep track of the frequency of individual characters, repeactly pop out the elements with the highest priority from the queue will ends up having a tree like structure which has nodes representing each character. By travering the tree we will be able to encode or decode the huffman codes. 


### Efficiency

Here I am using priority queue to encode the huffman tree based on the frequency of each individual character, the insertion takes O(1) time, but the removal takes O(n) time because the program needs to loop through the queue to find the element with the highest priority.

The time complexity of DFS if the entire tree is traversed is O(V) where V is the number of nodes. In the case of a graph, the time complexity is O(V+E) where V is the number of vertexes and E is the number of edges.

On average the encoding time complexity is O(n).

Decoding involves looping through the encoded data to decipher each character based on the mapping dictionary, on average it takes O(log k) node visits to decode a symbol. So the time complexity would be O(n logk).

This programs requires a dict to keep track of huffman binary code, a priority queue to pop out elements based on the frequency of the characters, and a tree to keep states of its left and right nodes. The tree contains k nodes, O(k) for the tree and O(n) for the decoded text.
