class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int):
        a=len(candies)
        Output=[]
        max_cand=max(candies)
        for i in range(a):
                if candies[i]+extraCandies>=max_cand:
                    Output.append(True)
                else:
                    Output.append(False)
        return Output