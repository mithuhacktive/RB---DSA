class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        current = 0
        maxi = 0

        for i in range(len(nums)):

            current += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            if i >= k:
                remove = nums[i - k]

                current -= remove
                freq[remove] -= 1

                if freq[remove] == 0:
                    del freq[remove]

            if i >= k - 1 and len(freq) == k:
                maxi = max(maxi, current)
        return maxi