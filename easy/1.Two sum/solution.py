class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash=defaultdict(lambda:-1)
        for x in range(len(nums)):
            complement=target-nums[x]
            if(hash[complement]==-1):
                hash[nums[x]]=x
            else:
                return [hash[complement],x]
