from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        lookup = Counter(s1)
        hashmap = {}
        left = 0
        right = 0
        while right < len(s2):
            if s2[right] in lookup:
                hashmap[s2[right]] = 1 + hashmap.get(s2[right], 0)
                
                while hashmap[s2[right]] > lookup[s2[right]]:
                    hashmap[s2[left]] -= 1
                    left += 1
                
                if len(s1) == (right - left + 1):
                    return True
                right += 1
            else:
                hashmap = {}
                right += 1
                left = right
            
        return False