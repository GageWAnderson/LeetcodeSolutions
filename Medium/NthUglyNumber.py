#Iterative Solution, was very confused by the problem statement
#The key to this problem is to use the prime factors to iteratively generate the numbers.
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2 = p3 = p5 = 0
        num = 1
        nums = [1]
        for i in range(n-1):
            choices = [nums[p2]*2, nums[p3]*3, nums[p5]*5]
            num = min(choices)
            nums.append(num)
            if choices[0] == num: p2 += 1
            if choices[1] == num: p3 += 1
            if choices[2] == num: p5 += 1
        
        return num

#To generate ugly numbers, keep multiplying by 2,3,or 5
#All ugly numbers are composed of some combonation of 2,3,5
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        p2,p3,p5 = 0,0,0
        while len(nums) < n:
            options = [nums[p2]*2, nums[p3]*3, nums[p5]*5]
            minVal = min(options)
            nums.append(minVal)
            if(minVal == options[0]): p2 += 1
            if(minVal == options[1]): p3 += 1
            if(minVal == options[2]): p5 += 1 #Need 3 ifs to account for duplicates
        return nums[-1]