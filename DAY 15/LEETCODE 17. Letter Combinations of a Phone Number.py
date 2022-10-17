class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        x = {1:[], 2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'],
            7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}
        
        #digits.length [0-4]
        n = len(digits)
        ans = []
        
        def twodig(d1,d2):
            x = []
            for i in d1:
                for j in d2:
                    x.append(i+j)
            return x
        
        def aa(digits,n):
            if n==0:
                return [""]
            else:
                return twodig(x[int(digits[0])] , aa(digits[1:],n-1))
        
        if n==0:
            return []
        
        return aa(digits,n)
        
        
        
        '''
        def twodig(d1,d2):
            x = []
            for i in d1:
                for j in d2:
                    x.append(i+j)
            return x
            
        if n==0:
            return []
        
        elif n==1:
            return x[int(digits)]
        
        else:
            ans = []
            res = []
            a = x[int(digits[0])]
            b = x[int(digits[1])]
            res = twodig(a,b)
            
            if n!=2:
                c = x[int(digits[2])]
                res = twodig(res,c)
    
                if n!=3: #n==4
                    d = x[int(digits[3])]
                    res = twodig(res,d)
            
            return res'''
