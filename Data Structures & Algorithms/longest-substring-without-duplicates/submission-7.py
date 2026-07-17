class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        maxStr = 0
        freq = {}
        left = 0
        right = 0

        while right < len(s):
            if s[right] not in freq:
                freq[s[right]] = 1
                maxStr = max(maxStr , (right - left + 1))
                right+=1
            else:
                if freq.get(s[left],0):
                    del freq[s[left]]
                left +=1



        return maxStr





        