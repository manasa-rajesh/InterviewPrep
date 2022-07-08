class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_digit(n):
            try:
                int(n)
                return True
            except ValueError:
                return  False
    
        operator = {'+': lambda x, y: int(x) + int(y),
                    '-': lambda x, y: int(x) - int(y),
                    '*': lambda x, y: int(x) * int(y),
                    '/': lambda x, y: int(int(x) / int(y))}
        stack = []
        for ele in tokens:
            if is_digit(ele):
                stack.append(ele)
            else:
                ele2 = stack.pop()
                ele1 = stack.pop()
                stack.append(operator[ele](ele1,ele2))
                
        return stack.pop()
        