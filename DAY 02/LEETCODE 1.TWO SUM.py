class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        hashmap = {}
        for i in range(l):
            diff = target - nums[i]
            if diff in hashmap:
                return [i,hashmap[diff]]
            else:
                hashmap[nums[i]] = i
        
