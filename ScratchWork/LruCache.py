class ListNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def __str__(self):
        curr = self.head
        sb = []
        while curr:
            if curr.val is None:
                sb.append("N")
            else:
                sb.append(str(curr.val))
            curr = curr.next
        return "->".join(sb)
    
    def insert_at_head(self, val):
        new_first_node = ListNode(val)

        prev_first_node = self.head.next
        self.head.next = new_first_node

        new_first_node.prev = self.head
        new_first_node.next = prev_first_node
        prev_first_node.prev = new_first_node

        return new_first_node
    
    def move_to_front(self, node):
        next_node = node.next
        prev_node = node.prev
        
        next_node.prev = prev_node
        prev_node.next = next_node

        self.insert_at_head(node.val)
    
    def remove_last_node(self):
        last_node = self.tail.prev

        if last_node == self.head:
            return # Can't remove from an empty list
        
        second_to_last_node = last_node.prev
        second_to_last_node.next = self.tail
        self.tail.prev = second_to_last_node
        return last_node.val[0] # Return the Key of the Removed Value


class LruCache:
    
    def __init__(self, capacity : int) -> None:
        self.capacity = capacity
        self.cache = dict()
        self.lru_list = LinkedList()
    
    def add(self, key, value):
        if key in self.cache:
            raise Exception("No Duplicates")
        new_node = self.lru_list.insert_at_head((key, value))
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            # Remove the Least-Recently-Used Node from LinkedList and Cache
            removed_key = self.lru_list.remove_last_node() 
            del self.cache[removed_key]
    
    def get(self,key):
        target_node = self.cache[key]
        self.lru_list.move_to_front(target_node)
        return target_node.val[1] # Value is the 1st element the the tuple (not the 0th)

import random
if __name__ == "__main__":
    CAPACITY = 10
    cache = LruCache(CAPACITY)

    for i in range(CAPACITY**2):
        key = random.randint(0, 100)
        value = random.randint(0, 100)
        try:
            cache.add(key, value)
            if cache.get(key) != value:
                print("Failed")
        except:
            print(f"Attempted to add duplicate key = {key}")
    
    print("Success")