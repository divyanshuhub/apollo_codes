class Solution:
    def heapHeight(self, N, arr):
        # code here
        x,i = 0,0
        while x<N:
            x += 2**i
            i+=1
        return i-1
