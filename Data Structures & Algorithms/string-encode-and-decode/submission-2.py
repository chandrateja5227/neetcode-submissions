class Solution:

    def encode(self, strs: List[str]) -> str:
        wholestring = []
        for s in strs:
            wholestring.append(f'{len(s)}#{s}')
        return ''.join(wholestring)




    def decode(self, s: str) -> List[str]:
        strings = []
        index = 0
        while index < len(s):
            curr = s.find('#',index)
            length = int(s[index:curr])
            start = curr + 1
            end =  curr + 1 + length
            strings.append(s[start:end])
            index = end

        return strings
