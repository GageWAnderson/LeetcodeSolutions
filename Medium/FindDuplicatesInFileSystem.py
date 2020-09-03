#Traverse the directory tree and use a dictionary to keep track of file content's
#You've already seen

#Didn't account for multiple files in one directory
#This problem was not very good...
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        def readFile(s): #Returns the file name as well as its content
            names = []
            contents = []
            
            i = 0
            path = []
            while s[i] != " ":
                path.append(s[i])
                i += 1
            path.append("/")
            
            i += 1
            while i < len(s):
                thisName = []
                thisContent = []

                while s[i] != "(":
                    thisName.append(s[i])
                    i  += 1
                i += 1

                while s[i] != ")":
                    thisContent.append(s[i])
                    i += 1
                i += 2
                names.append("".join(path + thisName))
                contents.append("".join(thisContent))
            
            return names,contents
        
        pathGroups = defaultdict(lambda : [],dict()) #Remember 1st arg is a lambda function
        for file in paths:
            names,contents = readFile(file)
            for i in range(len(names)):
                pathGroups[contents[i]].append(names[i])
        
        res = []
        for entry in pathGroups.values():
            if len(entry) > 1:
                res.append(entry)
        #Only list duplicates, so only return groups of greater than 1
        return res