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