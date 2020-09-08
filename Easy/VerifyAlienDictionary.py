class Solution: #O(nk), where k is the avg. length of words
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1: return True
        #Is there a more clever way than to hash the position of each letter?
        D = dict()
        for i in range(len(order)):
            D[order[i]] = i
        
        for i in range(1,len(words)):
            j = 0
            prev_word = words[i-1]
            curr_word = words[i]
            while j < len(prev_word) and j < len(curr_word):
                if D[prev_word[j]] > D[curr_word[j]]:
                    return False
                elif D[curr_word[j]] > D[prev_word[j]]:
                    break
                else:
                    j += 1
                    continue
            if j == len(curr_word) and j < len(prev_word): #shorter words come first
                return False
        return True