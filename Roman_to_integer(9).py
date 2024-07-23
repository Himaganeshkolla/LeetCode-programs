class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_arr=[] 
        sum_of_alp=0
        for i in s:
            char_arr.append(i)
        roman={
                'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000
                }
        for j in range(0,len(char_arr)):
            if (j+1)<len(char_arr):
                if roman[char_arr[j]]<roman[char_arr[j+1]]:
                    sum_of_alp-=roman[char_arr[j]]
                else:
                    sum_of_alp+=roman[char_arr[j]]
            else:
               sum_of_alp+=roman[char_arr[j]]
        return sum_of_alp
