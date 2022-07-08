class MergeSort:
    #Merge, mergesort must be in-place (stable sort, doesn't re-order initial order of otherwise equal elements)
    def _merge(self,arr : List[int], left : List[int], right : List[int]) -> None:
        if len(arr) > 1: #Base case do nothing
            #Since left,right are sorted, loops through both of them
            #And determines L>[i] R[j]
            i,j,k = 0,0,0
            #k tracks what index in arr you insert into
            while i < len(left) and j < len(right):
                if left[i] <= right[j]: #Make sure to use indicies not slicing
                    arr[k] = left[i] #Python slicing creates a copy, an expensive operation
                    i += 1
                else:
                    arr[k] = right[i]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        
    def mergeSort(self,arr : List[int]) -> None: #In place, so return None
        if len(arr) > 1:
            mid = len(arr)//2

            #Allocate temp L,R
            L = arr[:mid]
            R = arr[mid:]

            #Sort L,R, then merge them into arr
            self.mergeSort(L)
            self.mergeSort(R)
            self._merge(arr,L,R)