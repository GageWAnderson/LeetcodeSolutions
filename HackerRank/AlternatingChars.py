def alternatingCharacters(s):
    res = 0
    curr_run = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            curr_run += 1
        else:
            res += curr_run - 1
            curr_run = 1
    res += curr_run - 1
    return res