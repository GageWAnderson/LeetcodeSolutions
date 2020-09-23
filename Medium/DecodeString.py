#Better to do this iteratively with a stack to save space.

#Also, forgot to balance parens before recursing...
#This problem had a lot of small tricks in it, need to be more
#Careful when asking the interviewer questions about the problem...
class Solution:
    def decodeString(self, s: str) -> str: #O(n)
        print(f"s = {s}")
        sb = []
        i = 0
        while i < len(s):
            print(f"i = {i}")
            if s[i].isdigit():
                j = i
                while j<len(s) and s[j].isdigit():
                    j += 1
                k = int(s[i:j])

                start_index = j + 1
                j = j + 1
                count = 1 #Counts balanced parens
                print(f"j = {j}, k = {k}")
                while count > 0:
                    j += 1
                    if s[j] == "[":
                        count += 1
                    elif s[j] == "]":
                        count -= 1
                repeat = self.decodeString(s[start_index:j])
                
                for _ in range(k):
                    sb.append(repeat)
                    
                i = j + 1
            else:
                sb.append(s[i])
                i += 1
                
        return "".join(sb)