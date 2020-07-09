# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 02:52:46 2020

@author: vivek
"""
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children, plus a handler
        self.handler=handler
        self.children={}
        
    def insert(self, route):
        # Insert the node if not in children
        if route not in self.children:
            self.children[route]=RouteTrieNode()
            
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = handler
        
    def insert(self, paths,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node=self.root
        for path in paths:
            node.insert(path)
            node = node.children[path]
        node.handler = handler

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for path in paths:
            if path not in node.children:
                return None
            node = node.children[path]
        return node.handler
        
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, not_found_handler="404"):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routes = RouteTrie()
        self.routes.insert("/", handler)
        self.not_found = not_found_handler

    def add_handler(self, route, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        paths = self.split_path(route)
        self.routes.insert(paths, handler)

    def lookup(self, route):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        paths = self.split_path(route)
        return self.routes.find(paths) or self.not_found

    def split_path(self, route):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if len(route) == 1:
            return ["/"]
        else:
            return route.strip("/").split("/")

        
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print 'not found handler'

router.add_handler("/users/abcde", "user handler")  # add a route
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/users")) # should print 'not found handler'
print(router.lookup("/users/abcde")) # should print 'user handler'

router.add_handler("/srv/PRN/A4", "print A4 handler")  # add a route
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/srv")) # should print 'not found handler'
print(router.lookup("/srv/PRN/A4")) # should print 'print A4 handler'

router.add_handler("/srv/PRN/A3", "print A3 handler")  # add a route
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/srv/PRN/")) # should print 'not found handler'
print(router.lookup("/srv/PRN/A3/")) # should print 'print A3 handler'