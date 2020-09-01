from functools import cmp_to_key #This is how to do custom sort function with sorted
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs,key = cmp_to_key(self.compare)) #O(nlogn)
    
    # When providing a custom comparator, it should generally return an integer/float value
    # return a negative value (< 0) when the left item should be sorted before the right item
    # return a positive value (> 0) when the left item should be sorted after the right item
    # return 0 when both the left and the right item have the same weight and should be ordered "equally" without precedence
    def compare(self,log1,log2):
        log1Type = self.getLogType(log1)
        log2Type = self.getLogType(log2)
        #print(f"type1 = {log1Type}, type2 = {log2Type}")
        #Possible log types
        LETTER = 1 
        DIGIT = 0
        if log1Type == LETTER and log2Type == DIGIT:
            return -1
        elif log1Type == DIGIT and log2Type == LETTER:
            return 1
        elif log1Type == LETTER and log2Type == LETTER:
            i = 0
            while log1[i] != " ":
                i += 1
            j = 0
            while log2[j] != " ":
                j += 1
            
            log1Data = log1[i+1:]
            log2Data = log2[j+1:]
            log1ID = log1[:i]
            log2ID = log2[:j]
            cmp = self.compareData(log1Data,log2Data)
            if cmp: return cmp
            else:
                return self.compareData(log1ID,log2ID) #Tiebreaker w/ identifiers
            
        else: #Return digit logs in their original order
            return 1
    
    def compareData(self,log1,log2):
        #print(f"log1 = {log1}, log2 = {log2}")
        start = 0
        end = min(len(log1),len(log2))
        while start < end:
            if log1[start] > log2[start]:
                return 1
            elif log1[start] < log2[start]:
                return -1
            start += 1
        return None
    
    def getLogType(self,log):
        i = 0
        while i<len(log) and log[i] != " ":
            i += 1
        if log[i+1].isdigit():
            return 0
        else:
            return 1