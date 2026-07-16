class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        hashmap = {}

        result = 0
        left = 0
        right = 0
        maxK = 0
        while right <len(s):
            hashmap[s[right]] = 1 + hashmap.get(s[right],0)
          
            maxK = max(maxK ,  hashmap[s[right]])

            if (right - left + 1) - maxK > k :
                 hashmap[s[left]]-=1
                 left+=1

            result = max(result , (right - left + 1))
            right+=1

        return result





        