class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i==j:
                    break
                elif nums[i]+nums[j]==target:
                    return [i,j]
        