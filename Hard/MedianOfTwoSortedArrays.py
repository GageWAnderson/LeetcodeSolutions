import sys
class Solution: #Solution has the skeleton of binary search and the exit condition occurs
    #When all the elements on the left of i,j are less than all the elements on the right of i,j
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if(len(nums1)>len(nums2)):
            nums1,nums2=nums2,nums1
        
        X = len(nums1)
        Y = len(nums2)
        #print(X,Y)
        lw = 0
        high = len(nums1)
        
        while(lw<=high):
            
            partitinX = (lw + high) // 2
            partitinY = (X+Y+1) // 2 - partitinX
                 
            #print(partitinX,partitinY)
            leftX = -sys.maxsize-1 if(partitinX==0) else nums1[partitinX-1]
            leftY = -sys.maxsize-1 if(partitinY==0)  else nums2[partitinY-1]
            rightX = sys.maxsize if(partitinX==X) else nums1[partitinX]
            rightY = sys.maxsize if(partitinY==Y) else nums2[partitinY]
                
            if(leftX<=rightY and leftY<=rightX):
                print("fund",partitinX,partitinY)
                if((X+Y)%2==0):
                    return (max(leftX,leftY)+min(rightX,rightY))/2
                else:
                    #print(leftX)
                    return max(leftX,leftY)
                break
            elif(leftX>rightY):
                high = partitinX-1
            else:
                lw = partitinX+1

class MySolution: #Solution has the skeleton of binary search and the exit condition occurs
    #When all the elements on the left of i,j are less than all the elements on the right of i,j
#you only need to binary search in one of the arrays, the partition for the other array takes
#Care of itself
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(len(nums1)>len(nums2)): #Always do binary search on the shorter array to reduce runtime
            nums1,nums2=nums2,nums1
            
        m,n = len(nums1),len(nums2)
        if n == 0 and m == 0: return None
        if m == 0: return nums2[len(nums2)//2]
        if n == 0: return nums1[len(nums1)//2]

        A1Left,A1Right = 0,m
        while A1Left <= A1Right:
            i = A1Left + (A1Right - A1Left)//2
            j = (m + n + 1) // 2 - i #Location of j determined by i
            
            leftX = -inf if(i==0) else nums1[i-1]
            leftY = -inf if(j==0)  else nums2[j-1]
            rightX = inf if(i==m) else nums1[i]
            rightY = inf if(j==n) else nums2[j]
            
            if leftX <= rightY and leftY <= rightX:
                print(f"i = {i}, j = {j}")
                break
            elif leftX > rightY:
                A1Right = i - 1
            else:
                A1Left = i + 1
        
            if (m + n) % 2 == 0: #Need to account for if they are both oddd
                return (max(leftX,leftY)+min(rightX,rightY)) / 2
            else:
                return max(leftX,leftY)