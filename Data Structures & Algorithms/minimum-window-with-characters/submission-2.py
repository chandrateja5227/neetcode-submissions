from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        hash_map = Counter(t)
        left = 0
        freq = {}
        res = ""
        
        required = len(hash_map)
        formed = 0

        for right in range(len(s)):
            char = s[right]
            if char in hash_map:
                freq[char] = 1 + freq.get(char, 0)
                if freq[char] == hash_map[char]:
                    formed += 1
            
            while formed == required:
                if not res or (right - left + 1) < len(res):
                    res = s[left:right+1]
                
                left_char = s[left]
                if left_char in hash_map:
                    if freq[left_char] == hash_map[left_char]:
                        formed -= 1
                    freq[left_char] -= 1
                
                left += 1
                
        return res