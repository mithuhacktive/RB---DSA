class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t = sum(nums)
        l = 0
        
        for i , num in enumerate(nums):
            r = t-l-nums[i]
            
            if l == r:
                return i
            l+=num
        return -1
