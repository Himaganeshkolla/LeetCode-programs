class Solution():
    def isPalindrome(self, x):
        a=str(x)
        b=a[::-1] 
        if a==b:
            return "true"
        else:
            return "false"
       
            
