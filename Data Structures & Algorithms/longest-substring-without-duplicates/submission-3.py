class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        freq = {}
        left = 0
        result = 0

        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right],0)

            while freq.get(s[right]) > 1:
                freq[s[left]]-=1
                left +=1

            result = max(result , right - left + 1)

        return result
                

        