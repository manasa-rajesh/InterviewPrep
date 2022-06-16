class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        sum = 0
        i=0
        while(i<len(s)):
            curr = s[i]
            if i!=len(s)-1:
                nxt = s[i+1]

                if curr == 'I' and (nxt == 'V' or nxt =='X') :
                    val = dct[nxt] - dct[curr]
                    sum += val
                    i+=2

                elif curr == 'X' and (nxt == 'L' or nxt == 'C'):
                    val = dct[nxt] - dct[curr]
                    sum += val
                    i+=2

                elif curr == 'C' and (nxt == 'D' or nxt == 'M'):
                    val = dct[nxt] - dct[curr]
                    sum += val
                    i+=2
                else:
                    sum += dct[curr]
                    i+=1
                
            else:
                sum += dct[curr]
                i+=1
        return sum
            
        