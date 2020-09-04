#Sorting allows the search to be cut off past a certian point
#Use 2 pointers enclosing from either side cut off the search when the sums of the two pointers 
#Cross the target sum without touching it
class Solution: #O(n)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1,p2 = 0, len(numbers)-1

        while p1<p2:
            res = numbers[p1] + numbers[p2]
            if res == target:
                return [p1+1,p2+1]
            elif res < target:
                p1 += 1
            else:
                p2 -= 1
        return []