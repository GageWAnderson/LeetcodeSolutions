class Codec:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s # Length of String followed by delimiter
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 # Garunteed to find # delimiter since it's encoded
            strLen = int(s[i:j])
            res.append(s[j + 1: j + 1 + strLen])
            i = j + 1 + strLen # Set i to beginning of next String
        
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))