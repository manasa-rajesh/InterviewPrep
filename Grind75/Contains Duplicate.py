class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for ele in nums:
            if ele in dct.keys():
                return True
            else:
                dct[ele] = 1
        return False
        