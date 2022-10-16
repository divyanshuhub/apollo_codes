class Solution:
    def reverse(self, x: int) -> int:
        ss = str(x)
        sign = 1
        if ss[0]=='-':
            sign = -1
            s = ss[1:]
            print(s)
        else:
            s = ss
        print(s)
        while s[-1]=='0' and len(s)>1:
            if s[-1]==None:
                s[-1]=0
                break
            s = s[:-1]
        x = int(s[::-1])
        if sign == 1:
            if x>2147483647:
                return 0
            else:
                return x
        else:
            x = -x
            if x<-2147483648 :
                return 0
            else:
                return x
        
