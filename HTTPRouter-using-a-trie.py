from collections import defaultdict


class RouteTrie:
    def __init__(self, handler):
        self.root = RouteTrieNode()
        self.insert("/", handler)

    def insert(self, path, handler):
        road_listing = self.split_path(path)
        active_node = self.root
        for path in road_listing:
            active_node = active_node.children[path]
        active_node.handler = handler

    def find(self, path):
        road_listing = self.split_path(path)
        active_node = self.root
        for path in road_listing:
            if path not in active_node.children:
                return
            active_node = active_node.children[path]
        return active_node.handler

    def split_path(self, path):
        road_listing = path.split("/")
        road_listing[0] = "/"
        if road_listing[-1] == "":
            return road_listing[:-1]
        return road_listing


class RouteTrieNode:
    def __init__(self):
        self.children = defaultdict(RouteTrieNode)
        self.handler = None

    def insert(self):
        # Insert the node as before
        pass


class Router:
    def __init__(self, handler, notfound = None):
        self.route = RouteTrie(handler)
        self.notfound = notfound

    def add_handler(self, path, handler):
        if path == "" or not isinstance(path, str):
            return "Please input an valid path!"
        self.route.insert(path, handler)

    def lookup(self, path):
        if path == "" or not isinstance(path, str):
            return "Please input an valid path!"
        handler = self.route.find(path)
        return handler if handler is not None else self.notfound


# Here are some test cases and expected outputs you can use to test your implementation
# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
