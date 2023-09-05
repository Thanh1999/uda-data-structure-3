# uda-data-structure-3

### Problem 1:
1. Time and space complexities: 
- find_sqrt_number has O(log(n)) complexity because the binary search divides the search space in half at each step, reducing the search range exponentially
2. Algorithms: 
- Use binary search algorithm. 
- The find_sqrt_number calculates the midpoint of the search range using the begin and end value. If the square of midpoint is equal the number then it is the square root of that number. If not then if the square of midpoint is greatert than number we call find_sqrt_number again with the begin value is midpoint + 1 and end value is current end. Else we call find_sqrt_number with the begin is current begin and end value is midpoint - 1. The function is called recursively until begin value is bigger then end value. It will return None if it can't find the square root.

### Problem 2:
1. Time and space complexities: 
- rotated_array_search has O(log(n)) complexity because the binary search divides the list in half at each step, reducing the search range exponentially
- linear_search has O(n) complexity because it iterate through the list from first to last
2. Algorithms: 
- Use binary search algorithm. 
- The rotated_array_search take an input_list and the number we want to find its index. We then create a begin and value which are the first and last index of the input list. Then we find the midpoint index, if the value at midpoint is the number we want we retun directly else Since the list is rotated array the left or right sid from the midpoint index should be sorted - we can check it by compare the value at midpoint which the value at begin or end:
+ If the left half is sorted we then compare the number to check if it is between begin index value and midpoint index value. If it is we create new end index = midpoint - 1 else the begin index = midpoint + 1
+ If the right half is sorted we then compare the number to check if it is between midpoint index value and end index value. If it is we create new begin index = midpoint + 1 else the end index = midpoint - 1
Then we recursively do that loop until begin is bigger than end that we return index = -1 cause we can't find it

### Problem 3:
1. Time and space complexities: 
- O(nlog(n)) because the merge sort algorithm is used. The merge operation takes O(n) time, where n is the total number of elements in the two halves being merged. Since the merge operation is performed for each level of recursion, and there are log n levels of recursion in the merge sort algorithm, the overall time complexity is O(n log n).
2. Algorithms: 
- Use merge sort algorithm. 
- rearrange_digits use merge sort to dive the array into 2 half each step until each half array contains only 1 element then it will compare and merge it back by iterate through each sorted-half
- to create 2 numbers with biggest sum from a sorted descending array we will add interleave elements to each number. For example: The biggest to number1 and then 2nd biggest to number2 then 3rd biggest to number1...

### Problem 4:
1. Time and space complexities: 
- sort_012 has O(n) complexity, n is the total number of elements in the list
2. Algorithms: 
- Use Dutch partitioning algorithm
- We define three pointers: begin, mid, and end. The begin is the first index (0), the mid pointer is the current element being processed, and the end is the boundary of elements greater than the pivot. Then enter a while loop that continues until the mid pointer crosses the end pointer. Inside the loop, we check the value of the element at the mid pointer:

If it is 0, we swap it with the element at the begin pointer. This moves the 0 to the section of elements less than the pivot. Then increment both the begin and mid pointers.

If it is 1, we leave it in its place and simply increment the mid pointer. This maintains the section of elements equal to the pivot.

If it is 2, we swap it with the element at the end pointer. This moves the 2 to the section of elements greater than the pivot. We then decrement the end pointer to move backward.

We repeat steps 3 until the mid pointer crosses the end pointer, indicating that we have processed all elements.


### Problem 5:
1. Time and space complexities: 
- For Trie class:
+ insert function has O(n) complexity, where n is the length of the word being inserted
+ find function has O(n) complexity, where n is the length of the word being inserted
- For TrieNode class:
+ insert function has O(1) complexity casue we just add key to the dictionary
+ suffixes function has O(m) complexity, m the number of complete words below the current node
2. Algorithms: 
- Use Trie data structure
- Create a Trie data structure with a root node.
- Implement an insertion method that adds words to the Trie by creating new nodes for each character.
- Implement a search method that traverses the Trie to find a specific word.
- Implement an autocomplete method that traverses the Trie to find all words that match a given prefix.
- The autocomplete algorithm starts by traversing the Trie to the node representing the prefix. From that node, it performs a depth-first search to find all words bebegin it. The algorithm collects the words in a list and returns it as the autocomplete suggestions.

### Problem 6:
1. Time and space complexities:
- get_min_max has 0(n) complexity, n is the length of the list int
2. Algorithms:
- Use single traversal
- Assign the min, max value as the first element of the list. Iterate through the rest element, if there is element that bigger than max, max will be that new element. if there is element that smaller than min, min will be that new element

### Problem 7:
1. Time and space complexities: 
- RouteTrie class:
+ insert function has O(n) complexity, where n is the length of the path being inserted
+ find function has O(n) complexity, where n is the length of the path being searched
- RouteTrieNode class:
+ insert function has O(1) complexity casue we just add key to the dictionary
- Router class:
+ add_handler function has O(n) complexity, where n is the length of the path being added
+ lookup function has O(n) complexity, where n is the length of the path being looked up
+ split_path has O(1) complexity, simply split the path from a string
2. Algorithms:
- Use Trie data structure
- RouteTrie:
+ __init__(self, handler): This initializes the RouteTrie with a root node and a handler.
+ insert(self, path, handler): This method inserts a path and its associated handler into the trie. It recursively adds nodes to the trie for each part of the path.
+ find(self, path): This method navigates the trie to find a match for the given path and returns the associated handler. It traverses the trie based on each part of the path. 

- RouteTrieNode:
+ __init__(self): This initializes a RouteTrieNode with an empty dictionary for children and a handler.
+ insert(self, part): This method inserts a new child node for the given part.

Router:
+ __init__(self, root_handler, not_found_handler): This initializes the Router with a RouteTrie and a handler for 404 page not found responses.
+ add_handler(self, path, handler): This method splits the path into parts, and then adds the handler to the RouteTrie using the insert method.
+ lookup(self, path): This method splits the path into parts, and then looks up the handler in the RouteTrie using the find method. If the handler is not found, it returns the not found handler.
+ split_path(self, path): This method removes leading and trailing slashes from the path and splits it into parts.# uda-data-structure-3
