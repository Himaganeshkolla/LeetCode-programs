class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr=[]
        dict={}
        # for i in nums:
        count=0
        for i in range(0,len(nums)):
            count=0
            for j in range(0,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
            dict[nums[i]]=count
        print(dict)
        for i in nums:
            if (dict[i]>=2):
                arr.append(i)
            else:
                aa=nums.index(i)
                arr.append(nums[aa])
                arr.append(nums[aa+1])
                
