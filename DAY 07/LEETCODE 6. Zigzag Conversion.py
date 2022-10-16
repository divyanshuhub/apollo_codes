class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows==1:
            return (s)
        
        '''
        cycle = 2*numRows - 2
        strlist = []
        for i in range(numRows):
            for j in range(i, n, cycle):
                strlist.append(s[j])
                if i != numRows-1 and i != 0 and j+cycle-2*i < n:
                    strlist.append(s[j+cycle-2*i])             
        newstr = ''.join(strlist)
        return newstr'''
    
        if numRows==2:
            s1,s2='',''
            for i in range(n):
                if i%2==0:
                    s1 += s[i]
                    #print(s1,[],s2,n,s[i])
                else:
                    s2 += s[i]
                    #print(s1,[],s2,n,s[i])
            return s1+s2
        up = False
        down = True
        a = [[] for _ in range(numRows)]
        p = 0
        for i in range(n):
            ##print(a, s[i], p)
            a[p].append(s[i])
            
            if down:
                p+=1
            else:
                p-=1
            ##print(p)
            if p==numRows:
                ##print("p=",p,"down False")
                down = False
                p-=2
            elif p==0:
                ##print("p=",p,"down True")
                down = True
                #p+=1
        ans = ''
        for i in a:
            for j in i:
                ans += j
        ##print(ans)
        return ans
