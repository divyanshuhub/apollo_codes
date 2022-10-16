class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        def check(p,n,ans,ansl):
            if n==1:
                if ansl==1:
                    return ans,ansl

                if n>ansl:
                    ans=p
                    ansl = n
                    
                return ans,ansl
            if p==p[::-1]:
                
                if n>ansl:
                    ans=p
                    ansl = n
                    
                return ans,ansl
            return ans,ansl
        
        n = len(s)
        
        if n==1:
            return s[0]
        elif n==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        i = 0
        
        ans,ansl = "",0
        while (i<n):
            
            j = i+1
            while (j<=n):
                ss = s[i:j]
                
                ans,ansl = check(ss,j-i,ans,ansl)    
                if ansl>n-i:
                    return ans
                j += 1
            i += 1
            continue
                
        return ans
        '''
        
        
        #forward and backward check for palindrome
        def expand(s,left,right):
            while(left>=0 and right<len(s) and s[left]==s[right]):
                left-=1
                right+=1
            return right-left-1
        
        n = len(s)
        if n==1:
            return s[0]
        elif n==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        start, end = 0, 0
        for i in range(n):
            l = max(expand(s,i,i), expand(s,i,i+1))
            if l>end-start:
                start = i - int((l-1)/2)
                end = i + int(l/2)
        print(start,end)
        return s[int(start):int(end+1)]
            
