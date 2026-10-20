#doubly linked list for magaing the LRU part in O(1) time

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        #node id souble linked so it also has the prev
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        #hashmap to store key value pairs and retrieve them in O(1)
        self.d = {} #key: key, val: linked list value


        #init double linked list
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        next_ = node.next
        prev.next = next_
        next_.prev = prev

    def insert(self, node):
        #right is dummy, therefore put node just before right
        prev = self.right.prev #this precedes right, and will be preceding new node
        next_ = self.right #right will be the next of new node
        #put new node in between prev and right
        prev.next = node
        next_.prev = node
        node.prev = prev
        node.next = next_
        #prev -> new node -> self.right
        #prev <- new node <- self.right

    def get(self, key: int) -> int:
        if not key in self.d.keys(): return -1
        #return key, and also count this action as a new access to the key, so we have to put it at further right of the double linked list
        #this means: delete from linked list, and insert it at right
        node = self.d[key]
        self.remove(node)
        self.insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        #case:key aòready exists
        if key in self.d.keys():
            self.d[key].val = value
            #remove + reinsert, because this action coounts as a use
            self.remove(self.d[key])
            self.insert(self.d[key])
        else:
            #add to hashmap + linked list
            self.d[key] = Node(key, value)
            self.insert(self.d[key])


        #if len of linked list exceeds capacity, remove LRU node
        if len(self.d) > self.capacity:
            lru = self.left.next #element at left index +1, because self.left is a dummy node
            self.remove(lru)
            del self.d[lru.key]
        
