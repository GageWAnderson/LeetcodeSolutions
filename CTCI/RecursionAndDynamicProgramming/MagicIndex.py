import enum
from random import sample, randint

class MagicIndex:

    def __init__(self, n, minElem, maxElem, uniqueElements=True):
        if maxElem < n:
            raise Exception("maxElem must be greater than or equal to n.")
        elif uniqueElements:
            self.arr = sample(range(minElem, maxElem), n)
        else:
            self.arr = [randint(minElem, maxElem) for i in range(n)]

        self.arr.sort()
    
    # Finds the element in the array where A[i] = i
    def findMagicIndexBruteForce(self):
        for i,elem in enumerate(self.arr):
            if elem == i:
                return (i, elem)
        return None

    def findMagicIndexUniqueElements(self):
        left, right = 0, len(self.arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.arr[mid] == mid:
                return (mid, self.arr[mid])
            elif self.arr[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        return None
    
    def findMagicIndexNonUniqueElements(self):
        
        def binarySearchHelper(start, end):
            if end < start:
                return None
            mid = start + (end - start) // 2
            if self.arr[mid] == mid:
                return (mid, self.arr[mid])
            left = binarySearchHelper(start, min(mid - 1, self.arr[mid]))
            if left:
                return left
            right = binarySearchHelper(max(mid + 1, self.arr[mid]), end)
            if right:
                return right
            return None
        
        return binarySearchHelper(0, len(self.arr))
    
    def __str__(self):
        return str(self.arr)

if __name__ == "__main__":
    numTests = 10
    n, minElem, maxElem = 100,-200,200
    print("Testing unique-element arrays")
    for test in range(numTests):
        arr = MagicIndex(n, minElem, maxElem, True)
        print(arr.findMagicIndexBruteForce())
        print(arr.findMagicIndexUniqueElements())


    print("Testing non-unique element arrays")
    for test in range(numTests):
        arr = MagicIndex(n, minElem, maxElem, False)
        print(arr.findMagicIndexNonUniqueElements())
