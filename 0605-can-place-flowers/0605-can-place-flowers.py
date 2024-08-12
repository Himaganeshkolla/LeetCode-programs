class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
       # flowerbed = [1,0,0,0,1]
       #  n = 2
        flowerbed=[0]+flowerbed+[0]
        l=len(flowerbed)
        for i in range(1,l-1):
            if flowerbed[i]==flowerbed[i+1]==flowerbed[i-1]==0:
                n-=1
                flowerbed[i]=1
        # print(flowerbed)
        if n<=0:
            return True
        return False