from collections import defaultdict
#Not accounting for timestamps being lower in get()
#Need to look for the greatest timestamp in low less than timestamp and
#Return the value for that
class TimeMap:

    def __init__(self):
        self.D = defaultdict(list)        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.D[key].append((value,timestamp))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.D:
            return ""
        else:
            val_list = self.D[key]
            for i in range(len(val_list)-1,-1,-1): #Can replace w/ binary search
                this_timestamp = self.D[key][i][1]
                if this_timestamp <= timestamp:
                    return self.D[key][i][0]
            return ""

#The real solution for this problem is HashMap + Binary Search