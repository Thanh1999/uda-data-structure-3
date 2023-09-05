## A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = handler

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for part in path:
            if part not in current_node.children:
                current_node.insert(part)
            current_node = current_node.children[part]

        current_node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for part in path:
            if part not in current_node.children:
                return None
            current_node = current_node.children[part]

        return current_node.handler

## A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, part):
        # Insert the node as before
        self.children[part] = RouteTrieNode()


## The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
         # Create a new RouteTrie for holding our routes
        self.trie = RouteTrie(root_handler)
        
        # Add a handler for 404 page not found responses
        self.not_found_handler = not_found_handler
        
    def add_handler(self, path, handler):
       # Split the path into parts
        path_parts = self.split_path(path)
        
        # Add the handler to the RouteTrie
        self.trie.insert(path_parts, handler)
        
    def lookup(self, path):
        if not path:
            return self.not_found_handler
        # Split the path into parts
        path_parts = self.split_path(path)
        
        # Look up the handler in the RouteTrie
        handler = self.trie.find(path_parts)
        
        # If the handler is not found, return the not found handler
        if handler is None:
            return self.not_found_handler
        
        return handler
        
    
    def split_path(self, path):
         # Remove leading and trailing slashes, if any
        path = path.strip("/")
        
        if not path:
            return []
        # Split the path into parts
        path_parts = path.split("/")
        
        return path_parts


## Here are some test cases and expected outputs you can use to test your implementation

## create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

## some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

print("---Test cases---")
### Case found handler from path
router.add_handler("/search", "search handler") 
print(router.lookup("/search"))
# Expect search handler

### Case not found handler from path
print(router.lookup("/new"))
# Expect not found handler

### Case path is None
print(router.lookup(None))
# Expect not found handler