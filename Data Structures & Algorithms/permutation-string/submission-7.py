class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return False
            
        lookup = collections.Counter(s1)

        hash_map  = {}

        left  = 0

        for right in range(len(s2)):
            if s2[right] in lookup:
                hash_map[s2[right]] = 1 + hash_map.get(s2[right],0)

            if (right - left + 1) == len(s1):
                if lookup == hash_map:
                    return True
                if s2[left] in hash_map:
                     hash_map[s2[left]] -= 1
                     if hash_map[s2[left]] == 0:
                        del hash_map[s2[left]] 
                left+=1

        return False