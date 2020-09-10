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
    
    # Implementation of QuickSelect (Iterative)
    def kthSmallest(a, left, right, k) :  
    
        while left <= right :  
    
            # Partition a[left..right] around a pivot  
            # and find the position of the pivot  
            pivotIndex = partition(a, left, right)  
    
            # If pivot itself is the k-th smallest element  
            if pivotIndex == k - 1 :  
                return a[pivotIndex]  
    
            # If there are more than k-1 elements on  
            # left of pivot, then k-th smallest must be  
            # on left side.  
            elif pivotIndex > k - 1 : 
                right = pivotIndex - 1
    
            # Else k-th smallest is on right side.  
            else : 
                left = pivotIndex + 1
        
        return -1
  
# Driver Code 
arr = [ 10, 4, 5, 8, 11, 6, 26 ]  
n = len(arr)  
k = 5
print("K-th smallest element is",  
       kthSmallest(arr, 0, n - 1, k))  

    # To not panic in the interview, strictly follow this non in-place quick sort template.
    # For this question, the complete code: (Handles Duplicates)
    def quickselect(self,n, k):
        if k == 1:
            return [min(n,key = dist)]
        
        if k == len(n):
            return n

        pivot = choice(n)
        left = [i for i in n if dist(i) < dist(pivot)]
        mid = [i for i in n if dist(i) == dist(pivot)]
        right = [i for i in n if dist(i) > dist(pivot)]
        
        if len(left) > k:
            return quickselect(left,k)
        
        if len(left)<=k<=len(left)+len(mid):
            return left+mid[:k-len(left)]
        
        if len(left)+len(mid)<k:
            return left+mid+quickselect(right,k-len(left)-len(mid))
    
    def run(self):
        return self.quickselect(points,K)

#You can also use partitioning to sort part of an array for O(N) best-case and O(N^2) worst-case