class Solution():
    def isPalindrome(self, x):
#         a=str(x)
#         b=a[::-1]
        
#         if a==b:
#             return "true"
#         else:
#             return "false"
        if x < 0:
		    return False
        else:
	        return str(x) == str(x)[::-1]
       
            