class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        r=1
        maxprof=0
        while(r<len(prices)):
            if(prices[l]<prices[r]):
                maxprof=max(prices[r]-prices[l],maxprof)
            else:
                l=r
            r+=1
        return maxprof



        