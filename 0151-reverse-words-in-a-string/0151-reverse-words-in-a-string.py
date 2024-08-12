class Solution(object):
    def reverseWords(self, s):
        # a="the sky is blue"
        b=s.split()
        # print(b)
        x=b[::-1]
        # print(x)
        y=""
        for i in x:
            y=y+i+" "


        # print(y)

        if y[-1]==" ":
            y = y.rstrip()
            # y.replace(y[-1],"jbgldxz")     
        #     return x
        return y
