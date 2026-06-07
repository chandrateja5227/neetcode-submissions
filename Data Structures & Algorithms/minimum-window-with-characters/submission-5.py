from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        lookup  = Counter(t)
        freq = {}

        result = ""

        left = 0
        required = len(lookup)
        formed = 0
        for right in range(len(s)):
            if s[right] in lookup:
                freq[s[right]] = 1 + freq.get(s[right],0)
                if freq[s[right]] == lookup[s[right]]:
                    formed+= 1

            while formed == required:

                if not result or (right - left + 1) < len(result):
                    result = s[left:right+1]

                if s[left] in freq:
                    if freq[s[left]] == lookup[s[left]]: 
                        formed-= 1
                    freq[s[left]] -=1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                left+=1

        return result
