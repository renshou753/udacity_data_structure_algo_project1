#### Code Design

Here I am using recursion, in this problem a path may contain further subdirectories and there is no limit to the depth of the subdirectories can be. Each time I loop through the current directory I could get a list of files/folders. Recursion can be a good match for the problem because I need to go arbitrarily deep in order to all the files within each directory/subdirectory.

#### Efficiency

For the time complexity, it takes O(n) to loop through folders, O(n) to search for the files within each folder, depends on how deep the subdirectories can be the time can be O(m\*n) where m is the level of the subdirectories, n is the average files sitting in each subdirectory. I would assume O(n) time complexity on average.

Here I used a list to save the records matching the search criterials. Space would be O(n).
