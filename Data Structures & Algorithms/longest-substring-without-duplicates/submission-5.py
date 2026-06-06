class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hash_map = {}
        max_len = 0
        left  = 0
        count = 0
        for right in range(len(s)):
            hash_map[s[right]] = 1 + hash_map.get(s[right], 0)
                         
            while (right - left + 1) > len(hash_map):               
                hash_map[s[left]]-=1
                if hash_map[s[left]] == 0:
                    del hash_map[s[left]]
                left +=1
            max_len = max(max_len , right - left + 1)  
               
        return max_len



            






        