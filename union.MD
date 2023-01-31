#### Code design

For union, the program will loop through linked list 1 and linked list 2 one by one in order to get the union elements of the two.

For intersection, the program will loop through one linked list and search if the current element is in another list, if yes then this element will be added to the result.

#### Efficiency

For both union and intersection there are a number of loops including those to loop through the input linked list, also the one to search the result linked list which happens to be a loop. On average there will be x loops so average time efficiency will be O(n).

We need a linked list to keep track of the result, storage efficiency will also be O(n).
