class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        if len(s) != len(t):
            return False
        for ele in s:
            if ele in ds.keys():
                ds[ele] +=1
            else:
                ds[ele] = 1
        for ele in t:
            if ele not in ds.keys():
                return False
            if ele in dt.keys():
                dt[ele] +=1
            else:
                dt[ele] = 1
        print(ds)
        print(dt)
        for ele in t:
            if ds[ele] != dt[ele]:
                return False
        return True
                
        