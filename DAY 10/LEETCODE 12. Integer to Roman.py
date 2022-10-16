class Solution:
    def intToRoman(self, num: int) -> str:
        s = str(num)
        n = len(s)
        x = 0
        it = [['I','V','X'],['X','L','C'],['C','D','M'],['M','O','O']]
        def ex(a,x):
            low,high,lim = it[x]
            if a==0:
                return ''
            if a==1:
                return low
            if a==2:
                return low+low
            if a==3:
                return low+low+low
            if a==4:
                return low+high
            if a==5:
                return high
            if a==9:
                return low+lim
            if a in {6,7,8}:
                return high + ex(a-5,x)
            
            
        #i1 = ex(int(s[-1]),'I','V','X')    
        ans = []
        for i in range(1,n+1):
            i1 = ex(int(s[-i]),x) 
            x += 1
            print(i,s[-i],i1)
            ans.append(i1)
        print(ans)
        sss =''
        for i in ans[::-1]:
            sss += i
        return sss
            
        
