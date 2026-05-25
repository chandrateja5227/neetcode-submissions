from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashlist = defaultdict(list)

        for str in strs:
            key = tuple(sorted(str))
            hashlist[key].append(str)

        return [value for key, value in hashlist.items()]
