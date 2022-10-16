from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
               
        n = len(s)
        if n==0:
            return 0
        elif n==1:
            return 1
        
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans

    
####################
    
    
        chars = Counter()
        res,left,right = 0,0,0
        while right<n:
            r = s[right]
            chars[r] += 1
            
            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1
            
            res = max(res, right-left+1)
            
            right += 1
        return res
        
        
        
        
        
###################        
   
        
        
        
        def checkdupli(ss,nn):
            h = {}
            for j in range(nn):
                i = ss[j]
                if i in h:
                    return False
                else:
                    h[i] = j
            return True
        ans = 0
        for i in range(n):
            for j in range(i+ans+1,n+1):
                ts = s[i:j]
                nn = len(ts)
                if nn<=ans:
                    continue
                else:    
                    if checkdupli(ts,nn):
                        ans = max(len(ts),ans)
                    else:
                        break
        #print(ans)
        return(ans)
