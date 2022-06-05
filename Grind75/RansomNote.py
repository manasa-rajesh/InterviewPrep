class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = {}
        m = {}
        for ele in ransomNote:
            if ele in r.keys():
                r[ele] += 1
            else:
                r[ele] = 1
                
        for ele in magazine:
            if ele in m.keys():
                m[ele] += 1
            else:
                m[ele] = 1
                
        for ele in ransomNote:
            if ele not in m.keys():
                return False
            if m[ele] == 0:
                return False
            m[ele] -= 1
            
        return True