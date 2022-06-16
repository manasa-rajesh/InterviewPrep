class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        dct = {}
        for ele in nums:
            if ele in dct.keys():
                dct[ele] += 1
                if dct[ele] > n/2:
                    return ele
            else:
                dct[ele] = 1
                if dct[ele] > n/2:
                    return ele  
        