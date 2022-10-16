class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i in nums:
            if i in h:
                return True
            else:
                h[i] = 1
        return False
