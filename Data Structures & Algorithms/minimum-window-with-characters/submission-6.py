from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        hashmap = {}
        lookup = Counter(t)
        result = ""

        left = 0
        right = 0
        required = len(lookup)
        count = 0
        while right < len(s) or (count == required and left < len(s)):

            if count == required:
                if not result or (right - left) < len(result):
                    result = s[left:right]

                if s[left] in lookup:
                    if hashmap[s[left]] == lookup[s[left]]:
                        count -= 1
                    hashmap[s[left]] -= 1
                left+=1
            else:
                if s[right] in lookup:
                    hashmap[s[right]] = 1 + hashmap.get(s[right] , 0)
                    if hashmap[s[right]] == lookup[s[right]]:
                        count+=1

                right+=1

        return result