class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        value = 0
        for i in range(len(nums)):
            value += nums[i]
            if value > s:
                s = value
            if value < 0:
                value = 0
        if max(nums)<0:
            return max(nums)
        return s