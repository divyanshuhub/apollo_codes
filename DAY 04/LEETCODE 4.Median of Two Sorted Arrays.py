class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1 + nums2
        l.sort()
        n = len(l)
        if n % 2 == 0:
            
            return float((l[int(n/2) -1] + l[int(n/2)])/2)
        else:
            return float(l[n//2])
          
#############################################

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1,l2 = len(nums1), len(nums2)     
        l = l1 + l2
        if l%2 == 0:
            even = True
            l = [l/2 - 1, l/2]
        else:
            even = False
            l = [int(l/2)]
        #print(even,l)
        #f = []
        a = []
        i,j,t = 0,0,0
        a,med = 0,0
        
        
            
            
        while i<l1 or j<l2:
            if i<l1:
                n1 = nums1[i]
                if j<l2:
                    n2 = nums2[j]
                    if n1<=n2:
                        if t in l:
                            if even:
                                a += n1
                                med += 1
                                if med==2:
                                    return float(a/2)
                            else:
                                return float(n1)
                        #f.append(n1)
                        t+=1
                        i += 1
                    else:
                        if t in l:
                            #a.append(n2)
                            if even:
                                a += n2
                                med += 1
                                if med==2:
                                    return float(a/2)
                            else:
                                return float(n2)
                        #f.append(n2)
                        t+=1
                        j += 1
                else:
                    if t in l:
                        #a.append(n1)
                        if even:
                            a += n1
                            med += 1
                            if med==2:
                                return float(a/2)
                        else:
                            return float(n1)
                    #f.append(n1)
                    t+=1
                    i += 1  
            else:
                n2 = nums2[j]
                if t in l:
                    #a.append(n2)
                    if even:
                        a += n2
                        med += 1
                        if med==2:
                            return float(a/2)
                    else:
                        return float(n2)
                #f.append(n2)
                t+=1
                j += 1
            
        print(f)
        print(a)
        return 2.0
            
            
 
