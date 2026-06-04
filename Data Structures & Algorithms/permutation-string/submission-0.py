
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        hash_set = Counter(s1)
        freq = {}
        left = 0
        window = len(s1)
        for right in range(len(s2)):
            freq[s2[right]] = 1 + freq.get(s2[right],0)

            if len(s1) == right - left + 1:
                if hash_set == freq:
                    return True
                freq[s2[left]] -=1
                if freq[s2[left]] == 0:
                    del freq[s2[left]]
                left+=1

         
        return False

            
                
        