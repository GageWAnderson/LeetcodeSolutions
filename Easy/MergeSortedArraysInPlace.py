#This is a tedious 2-pointers problem
#Basically, just merge from mergesort (3 while loops)
#Start from end to avoid overwriting
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1,p2 = m-1,n-1
        p = m + n -1 #Where points are inserted
        
        while p1 >=0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
            
        #Add the remaining elements from nums2
        while p2 >= 0:
            nums1[p2] = nums2[p2]
            p2 -= 1

#Start from end