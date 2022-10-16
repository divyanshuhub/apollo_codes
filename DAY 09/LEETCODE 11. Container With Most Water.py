class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n-1
        def area(l,r): 
            return  (r - l) * min(height[l],height[r])
            
        ar = area(left,right)
        
        while left<right:
            ari = area(left,right)
            ar = max(ar,ari)
            if height[left]<=height[right]:
                left += 1
            else:
                right -= 1
        return ar
                
                
                
