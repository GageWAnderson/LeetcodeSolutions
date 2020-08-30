import random
class QuickSelect:
    #Standard partition, considers last element as the pivot
    #And moves all smaller elements to its left greater to right
    def partition(self,arr,l,r,pivotIndex):
        pivot = arr[pivotIndex]
        pivot,arr[r] = arr[r],pivot #Store pivot to the right
        i = l
        for j in range(l,r):
            if arr[j] <= pivot:
                arr[i],arr[j] = arr[j],arr[i]
                i += 1

        arr[i],arr[r] = arr[r],arr[i] #Swap pivot back into position
        return i

    #Recursive implementation, I prefer iterative as no change to k is required
    def kthSmallest(self,arr,l,r,k): 
        if k <= 0 or k >= len(arr):
            raise Exception("k must be in [1,len(arr)] to be valid.")
        
        pivotIndex = random.randint(l,r) #Choose a random pivot
        index = self.partition(arr,l,r,pivotIndex)

        if index - l == k-1:
            return arr[index]
        elif index - l > k - 1: #If position is more than k, recur for right subarray
            return self.kthSmallest(arr,l,index-1,k)
        else: #Else, recur for the left subarray
            return self.kthSmallest(arr,index+1,r,k-index+l-1)