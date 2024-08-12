class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=None
        count=0
        for i in nums:
            if count==0:
                ans=i
            if i==ans:
                count+=1
            else:
                count+=-1
        return ans
    