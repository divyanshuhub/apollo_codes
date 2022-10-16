class Solution:
    def myAtoi(self, s: str) -> int:
        
        if s=='':
            return 0
        while s[0] ==' ':   #not in {'1','2','3','4','5','6','7','8','9'}:
            s = s[1:]
            if s=='':
                return 0
        if s[0]==None:
            return 0
        
        sign = 1
        if s[0]=='-':
            sign = -1
            s = s[1:]
        elif s[0]=='+':
            s = s[1:]
        
        ans = ''
        print(s)
        for i in s:
            if i.isdigit():
                ans += i
            else:
                break
            '''try:
                if type(int(i)) == int:
                    ans += i
            except:
                #pass
                break'''
        print(ans)
        if ans=='':
            return 0
        x = int(ans)
        
        if sign == 1:
            if x>2147483647:
                return 2147483647
            else:
                return x
        else:
            x = -x
            if x<-2147483648 :
                return -2147483648
            else:
                return x
        
