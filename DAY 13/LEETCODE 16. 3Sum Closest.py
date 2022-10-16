class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        print(nums)
        d = 99999
        for i in range(n-2):
            r = n-1
            l = i+1
            left = nums[l]
            right = nums[r]
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                diff = abs(s-target)
                #print(i,l,r,s,target,diff,d)
                #print(nums[i] , left , right)
                if diff<d:
                    d=diff
                    ans=s
                if s>target:
                    r-=1  
                elif s<target:
                    l+=1
                else:
                    return s
        return ans
