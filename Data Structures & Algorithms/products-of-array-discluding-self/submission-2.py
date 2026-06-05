class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        p = 1
        for i in range(0,n-1):
            p = p*nums[i]
            res[i+1] = p
        p = 1
        for i in range(n-1,-1,-1):
            res[i] *= p
            p *= nums[i]
        
        return res