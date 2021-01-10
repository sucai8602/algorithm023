class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        for num in nums:
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
