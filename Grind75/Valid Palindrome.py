class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        if len(s) < 2:
            return True
        if len(s) % 2 == 0:
            each = len(s)/2
        else:
            each = (len(s)-1)/2
        print(each)
        first = s[0:int(each)]
        print(first)
        last = s[-(int(each)):]
        print(last[::-1])
        
        if first == last[::-1]:
            return True
        else:
            return False
        