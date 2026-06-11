class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        st = set()
        l = 0
        r = 1
        ml = 1
        while r<=len(s):
            if len(s[l:r]) == len(set(s[l:r])):
                ml = max(ml,len(s[l:r]))
                r+=1
            else:
                l+=1
        
        return ml
        