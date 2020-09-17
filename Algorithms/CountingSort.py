#Counting sort is only useful when there is a SMALL
#Counting sorte is efficient if the range of input data is not that much greater than num_objects to be sorted
#Cap on the size of the elements in the array
#O(nk), where k is the maximum value
from collections import Counter
import copy
class CountSort:
    def count_find(self,A : List[int],max_val : int, idx : int): #Requires that the max val in A is small
        s = 0
        counter = Counter(A) #O(n)
        for i in range(0,max_val):
            freq += counter[i]
            s += freq
            if s >= idx:
                return i

    def count_sort(self,A : List[int], max_val : int): #Exclusive of max_val
        counter = Counter(A)
        output_arr = [0 for i in range(max_val)]
        for num in range(1,max_val):
            counter[num] += counter[num-1]

        #Now, build the sorted output array
        for i in range(len(A)):
            output_arr[counter[arr[i]]-1] = arr[i]
            counter[arr[i]] -= 1

        A = copy.deepcopy(output_arr) #Destructive of A
        return A