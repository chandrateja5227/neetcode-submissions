import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        string = re.sub(r'[^a-zA-Z0-9]', '', s,).lower()

        i = 0
        j = len(string)-1
        print(string)
        while i < j:
            if string[i] == string[j]:
                i+=1
                j-=1
            else:
                return False

        return True

         
        