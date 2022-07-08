class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def twosum(nums,l,r,val):
            pairs = []
            while(l<r):
                if nums[l] + nums[r] +val == 0:
                    pairs.append([l,r])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif nums[l] + nums[r] +val < 0:
                    l+=1
                else:
                    r-=1
            return pairs
            
        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            l = i+1
            r = len(nums) -1
            pairs = twosum(nums,l,r,nums[i])
            if len(pairs)>0:
                for pair in pairs:
                    res.append([nums[i],nums[pair[0]],nums[pair[1]]])
        return res