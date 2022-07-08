class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringset = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in stringset:
                stringset.remove(s[l])
                l += 1
            stringset.add(s[r])
            res = max(res,r-l+1)
        return res
        