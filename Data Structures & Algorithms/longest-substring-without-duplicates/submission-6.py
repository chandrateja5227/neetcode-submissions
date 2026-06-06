from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_index = defaultdict(int)
        left = 0
        right = 0
        max_len = 0
        while right < len(s):
            if s[right] in hash_index:
                next_index = hash_index.get(s[right])
                while left < next_index + 1:
                    del hash_index[s[left]]
                    left+=1
               
                hash_index[s[right]] = right
                right+=1
            else:
                hash_index[s[right]] = right
                max_len = max(max_len,len(hash_index))
                right+=1

        return max_len







        