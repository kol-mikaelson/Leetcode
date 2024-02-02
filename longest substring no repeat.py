class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        l = []
        for i in s:
            if i in l:
                if len(l) > max:
                    max = len(l)
                cont = l.index(i)
                while cont >= 0:
                    l.pop(cont)
                    cont -= 1
                l.append(i)
            else:
                l.append(i)
        if len(l) > max:
            max = len(l)
        return max
