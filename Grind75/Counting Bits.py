import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]*(n+1)
        exp = 1
        
        for i in range(1,n+1):
            if exp*2==i:
                exp=i
            result[i] = 1 + result[i-exp]
            
        return result
                
        
        
        