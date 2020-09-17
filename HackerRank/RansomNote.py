# Complete the checkMagazine function below.
# Just create counters for each of the words
# And check for overlap
from collections import Counter #Hashing case-sensitive?
def checkMagazine(magazine, note):
    mag_count = Counter(magazine)
    note_count = Counter(note) #O(n)
    for word in note:
        if mag_count[word] < note_count[word]:
            print("No")
            return
    print("Yes")
    return