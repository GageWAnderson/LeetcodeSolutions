#You can do iterative DFS and add paths to the stack
#Or you can do recursive DFS and remember the paths
#Use a string builder to add letters to a sequence
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        res = []
        letterDict = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        
        def getNextLetters(s,i):
            if i == len(s):
                return []
            else:
                ans = []
                for letter in letterDict[s[i+1]]:
                    res.append(letter)
                return ans
        
        def dfs(i,s,path):
            if i == len(s):
                res.append("".join(path))
            else:
                for letter in letterDict[s[i]]:
                    dfs(i+1,s,path+[letter])
                  
        dfs(0,digits,[]) #Made this void
        return res

#Not converting to int doubled my speed!