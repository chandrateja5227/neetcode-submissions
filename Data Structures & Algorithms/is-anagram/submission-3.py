class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1 = {}
        hash2 = {}

        for i in s:
            if hash1.get(i):
                hash1[i] +=1
            else:
                 hash1[i] =1

        for i in t:
            if hash2.get(i):
                hash2[i] +=1
            else:
                 hash2[i] =1


        return hash1 == hash2

        

        