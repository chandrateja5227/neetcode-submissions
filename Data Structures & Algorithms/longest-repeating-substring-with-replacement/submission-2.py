class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        hash_map = {}
        maxf = 0
        left  = 0
        result = 0

        for right in range(len(s)):
            hash_map[s[right]] = 1 + hash_map.get(s[right],0)
            maxf  = max(maxf , hash_map[s[right]])

            if (right - left + 1) - maxf > k:
                hash_map[s[left]] -= 1 
                left +=1

            result  = max(result ,(right - left + 1))

        return result