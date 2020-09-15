#Set not a counter, read the question more carefully!
#Also, this just tests your knowledge of the random library
import random
class RandomizedSet:
    #This is just a list with a hash set of indexes
    def __init__(self):
        self.num_set = set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.num_set:
            return False
        else:
            self.num_set.add(val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.num_set:
            return False
        else:
            self.num_set.remove(val)
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        #Notably, arbitrary != random
        num = random.sample(self.num_set,1) #You don't have to remove the element from the set
        #Apparently, random.sample() is O(n)
        return num[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

#Much faster solution was my first idea, use a hash map + list

#First thought would be using a set, however using an ArrayList with
#Indicies of elements in a set would be the fastest

#Average O(1), worst-case O(n) since the list will sometimes have to
#Resize on insertion/deletion
from random import randint
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elems = []
        self.index_set = dict()
        self.removed_indicies = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.index_set:
            self.elems.append(val)
            self.index_set[val] = len(self.elems) - 1
            return True
        else:
            return False
        
    #Idea, replace with the last element
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.index_set:
            index = self.index_set[val] #Indicies are wrong once self.elems is updated
            if index == len(self.elems)-1:
                self.elems.pop()
            else:
                last_elem = self.elems.pop()
                self.elems[index] = last_elem
                self.index_set[last_elem] = index
            del self.index_set[val]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        rand_index = randint(0,len(self.elems)-1)
        return self.elems[rand_index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()