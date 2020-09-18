# Complete the countInversions function below.
# Implement merge-sort, count the number of inversions
# If index in merged array does not match index in left,right a swap occured
def countInversions(arr):
    num_inversions = [0]

    def merge(arr,left,right):
        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                num_inversions[0] += len(left) - i
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

    def mergeSort(arr): #end is disclusive
        if len(arr) <= 1:
            return
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        mergeSort(left)
        mergeSort(right)
        merge(arr,left,right)

    mergeSort(arr) #Auto-updates num_inversions
    return num_inversions[0]