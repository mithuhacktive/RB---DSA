class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = sum(nums[:k])
        maximum = current
        for i in range(len(nums)-k):
            current += nums[i+k] - nums[i] 
            maximum = max(maximum , current)
        return maximum/k