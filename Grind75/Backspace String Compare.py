class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        
        for ele in s:
            if len(s1) == 0 and ele == '#':
                continue
            elif ele == '#':
                s1.pop()
            else:
                s1.append(ele)
        
        for ele in t:
            if len(s2) == 0 and ele == '#':
                continue
            elif ele == '#':
                s2.pop()
            else:
                s2.append(ele)
                
        print(s1)
        print(s2)
        if s1 == s2:
            return True
        else:
            return False