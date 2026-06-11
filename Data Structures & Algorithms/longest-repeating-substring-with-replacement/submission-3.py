class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 1
        ml = 0
        while r<=len(s):
            d = {}
            freq = [[] for i in range(len(s[l:r])+1)]
            for n in s[l:r]:
                d[n] = 1+d.get(n,0)

            mx = max(d.values())
            if len(s[l:r])-mx<=k:
                ml = max(ml,len(s[l:r]))
                r+=1
            else:
                l+=1
            
        return ml