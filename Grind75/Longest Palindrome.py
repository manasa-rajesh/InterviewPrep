class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        dct = {}
        for ele in s:
            if ele in dct.keys():
                dct[ele] += 1
            else:
                dct[ele] = 1
                
        cnt = list(dct.values())
        
        for i in range(len(cnt)):
            if cnt[i] == 1:
                continue
            elif cnt[i] % 2 == 0:
                length += cnt[i]
                cnt[i] = 0
            else:
                length += cnt[i] - 1
                cnt[i] = 1
                
        if max(cnt) == 0:
            return length
        else:
            return length+1