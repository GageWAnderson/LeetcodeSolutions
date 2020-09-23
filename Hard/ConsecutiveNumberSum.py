class SolutionSlow:
    def expandFromMiddle(self,nums,i,seen,target): 
        res = 0
        j = i + 1
        total_right = nums[i]
        while j < len(nums): #Look right
            total_right += nums[j]
            #print(f"total_right = {total_right}")
            if (i,j) in seen:
                j += 1
                continue
            seen.add((i,j))
            
            if total_right == target:
                res += 1
                break
            elif total_right > target:
                break
            else:
                j += 1
                
        j = i - 1
        total_left = nums[i]
        while j >= 0: #Look left
            total_left += nums[j]
            if (j,i) in seen:
                j -= 1
                continue
            seen.add((j,i)) 
            
            if total_left == target:
                res += 1
                break
            elif total_left > target:
                break
            else:
                j -= 1
                
        j,k = i - 1, i + 1
        total_mid = nums[i]
        while j >= 0 and k < len(nums): #Look from middle
            total_mid += nums[j] + nums[k]
            if (j,k) in seen:
                j -= 1
                k += 1
                continue
            seen.add((j,k))
                
            if total_mid == target:
                res += 1
                break
            elif total_mid > target:
                break
            else:
                j -= 1
                k += 1
        return res
    
    def consecutiveNumbersSum(self, N: int) -> int: #O(n^2)
        nums = [i for i in range(1,(N//2)+2)]
        res = 1 #Include the number itself
        seen = set()
        for i in range(len(nums)):
            res += self.expandFromMiddle(nums,i,seen,N)
        return res

class SolutionCompleteSquare:
    #This is really just a math problem, some simple algebra could figure this out...
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        # x > 0 --> N/k - (k + 1)/2 > 0
        upper_limit = ceil((2 * N + 0.25)**0.5 - 0.5) + 1
        for k in range(1, upper_limit):
            # x should be integer
            if (N - k * (k + 1) // 2) % k == 0:
                count += 1
        return count