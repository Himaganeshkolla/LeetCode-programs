class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        arr1=heights[:]
        arr1.sort(reverse=True)
        arr_index=[]
        names_demo=[]
        for i in arr1:
            arr_index.append(heights.index(i))
#         print(arr_index)
        for i in arr_index:
            names_demo.append(names[i])
        
        return names_demo
            
