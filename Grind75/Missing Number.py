class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = max(nums)
        for i in range(n):
            if i in nums:
                continue
            else:
                return i
        
        return n+1