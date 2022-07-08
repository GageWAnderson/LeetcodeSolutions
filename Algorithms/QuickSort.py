# Python program for implementation of Quicksort Sort 
class QuickSort:
    # This function takes last element as pivot, places 
    # the pivot element at its correct position in sorted 
    # array, and places all smaller (smaller than pivot) 
    # to left of pivot and all greater elements to right 
    # of pivot 
    def __init__(self):
        pass

    def partition(self,arr,low,high): 
        i = ( low-1 )         # index of smaller element 
        pivot = arr[high]     # pivot 
    
        for j in range(low , high): 
    
            # If current element is smaller than the pivot 
            if   arr[j] < pivot: 
            
                # increment index of smaller element 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
    
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 ) 
    
    # The main function that implements QuickSort 
    # arr[] --> Array to be sorted, 
    # low  --> Starting index, 
    # high  --> Ending index 
    
    # Function to do Quick sort 
    def quickSort(self,arr,low,high): 
        if low < high: 
    
            # pi is partitioning index, arr[p] is now 
            # at right place 
            pi = self.partition(arr,low,high) 
    
            # Separately sort elements before 
            # partition and after partition 
            self.quickSort(arr, low, pi-1) 
            self.quickSort(arr, pi+1, high) 

if __name__ == "__main__":
    qs = QuickSort()
    arr = [12,45,5,6,43256,6,54,54,6,7,435,6,34,5435,7,53245,5,453]
    print(arr)
    qs.quickSort(arr,0,len(arr)-1)
    print(arr)