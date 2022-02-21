class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = [0] * len(nums)
        a[0] = nums[0]
        for i in range(1, len(nums)):
            a[i] = max(nums[i], a[i-1] + nums[i])
        
        # print(a)
        return max(a)
