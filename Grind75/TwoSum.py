class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        result = []
        for i in range(len(nums)):
            dct[nums[i]] = i
        for i in range(len(nums)):
            if(target-nums[i] in dct.keys()):
                if i != dct[target-nums[i]]:
                    result.append(i)
                    result.append(dct[target-nums[i]])
                    break
        return result