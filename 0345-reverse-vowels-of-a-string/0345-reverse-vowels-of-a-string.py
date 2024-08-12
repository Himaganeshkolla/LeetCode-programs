class Solution(object):
    def reverseVowels(self, s):
        s1=list(s)
        # print(s1)
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        a=[]
        b=[]
        for i in s1:
            if i in vowels:
                a.append(i)
        a.reverse()
        k=0
        for j in range(len(s)):
            if s1[j] in vowels:
                s1[j]=a[k]
                k+=1
        x=""
        for i in s1:
            x=x+i
        return x
