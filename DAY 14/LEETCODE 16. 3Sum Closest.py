class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n,z,p = [],[],[]
        nc,zc,pc = 0,0,0
        ans = set()
        for i in nums:
            if i<0:
                n.append(i)
                nc += 1
            elif i==0:
                z.append(i)
                zc += 1
            else:
                p.append(i)
                pc += 1
        
        
        #for faster look ups
        setp = set(p)
        setn = set(n)
        
        print(nums)
        print(n,z,p)
        print(nc,zc,pc)
        print(setp,setn)
        
        
        # -ve 0 +ve combo
        if zc>0:
            for i in n:
                if -i in setp:
                    ans.add((i,0,-i))
        
        # 0 0 0 combo
        if zc>2:
            ans.add((0,0,0))
        
        # -ve -ve +ve combo
        for i in range(nc):
            for j in range(i+1,nc):
                a,b = n[i], n[j]
                c = (a+b)
                if -c in setp:
                    ans.add(tuple(sorted([a,b,-c])))
                    
        # -ve +ve +ve combo
        for i in range(pc):
            for j in range(i+1,pc):
                a,b = p[i], p[j]
                c = (a+b)
                if -c in setn:
                    ans.add(tuple(sorted([-c,a,b])))
        return (ans)
                    
        
        
        
