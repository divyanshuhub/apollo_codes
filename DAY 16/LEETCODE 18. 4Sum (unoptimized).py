class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        a = set()
        for i in range(n-3):
            main = i+1
            l,r = main+1, n-1
            t1 = nums[i]
            while l<r and main<n:
                #print(i,main,l,r)
                t2 = nums[main] + nums[l] + nums[r]
                tt = t1 + t2
                #print([nums[i], nums[main], nums[l], nums[r]],sum([nums[i], nums[main], nums[l], nums[r]]))
                if tt == target:
                    #ans.append([nums[i], nums[main], nums[l], nums[r]])
                    a.add(tuple(sorted([nums[i], nums[main], nums[l], nums[r]])))
                    l += 1
                elif tt<target:
                    l += 1
                else: #tt>target:
                    r -= 1
                        
                if l>=r:
                    main += 1
                    l,r = main+1, n-1
                    t1 = nums[i]
        
        for i in a:
            ans.append(i)
        print(ans)
        return ans
