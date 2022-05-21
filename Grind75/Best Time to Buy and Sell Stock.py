class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = 2**31 - 1
        profit = 0
        
        for ele in prices:
            if ele<minprice:
                minprice = ele
            else:
                if ele-minprice > profit:
                    profit = ele-minprice
        return profit