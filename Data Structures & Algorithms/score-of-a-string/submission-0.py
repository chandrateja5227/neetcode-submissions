class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 1
        total = 0
        while i < len(s):
            total += abs(ord(s[i-1]) - ord(s[i]))
            i+=1

        return total   

        