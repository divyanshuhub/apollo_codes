class Solution:
    def romanToInt(self, s: str) -> int:
        
        x = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        a,p,n = 0,x[s[0]],0
        for i in s:    
            if p<x[i]:
                a += x[i] - 2*p
            else:
                a += x[i]
            p = x[i]  
        return a
        
        '''
        a = 0
        n = len(s)
        x = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1,'O':0}
        s += "OO"
        j = 0
        while j < n:
            i = s[j]
            if x[s[j+1]]>x[s[j]]:
                a +=  x[s[j+1]] - x[s[j]]
                j += 2
                continue
            a += x[i]
            j += 1
        return a'''
