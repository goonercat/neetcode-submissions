class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        lst = []
        i = 0
        for i in range(n-2):
            l = i+1
            r = n-1
            if i>0 and nums[i-1] == nums[i]:
                continue
            while l<r:
                if nums[i]+nums[l]+nums[r]>0:
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    lst.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1

                        
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1

        return lst
                    