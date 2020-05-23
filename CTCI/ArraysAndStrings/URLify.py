#CTCI 1.3
#Idea here is to use the string builder data structure to reduce the time complexity
#Of concatenating all the strings together with "%20"

def urlify(s):
    if len(s) == 0: return s
    sections = []
    start = 0
    for i in range(len(s)):
        if s[i] == " ":
            sections.append(s[start:i]) #Indexing is end-disclusive 
            start = i + 1
    #What to do at the end of the string?
    sections.append(s[start:len(s)]) #Appends the last item
    print(sections)
    res = ""
    for i in range(len(sections)-1):
        res = res + sections[i] + "%20" + sections[i+1]
    return res

if __name__ == "__main__":
    print(urlify("hello world"))
    print(urlify(" "))
    print(urlify("Mr John Smith  "))

#Solution notes:
#Since strings are immutable, we need to return a new copy of the string at the end
#Using character arrays would allow for better memory management with a 2-scan approach

#First scan sets the size of the array to the number of non-space characters = 3*number of spaces
#Second pass fills in the character array, then turns it into a string 