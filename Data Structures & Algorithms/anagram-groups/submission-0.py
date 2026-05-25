from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashlist = {}

        for str in strs:
            if hashlist.get(tuple(sorted(str))):
                hashlist[tuple(sorted(str))].append(str)
            else:
                hashlist[tuple(sorted(str))] = [str]

        return [value for key , value in hashlist.items()]