class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        st = set(nums)
        n = len(nums)
        l = 1
        for i in range(n):
            if nums[i]-1 in st:
                continue
            else:
                d = 1
                x = nums[i]+1
                
                while x in st:
                    d+=1
                    x+=1
                    print(x)
                
                if d>l:
                    l = d
            
        
        return l