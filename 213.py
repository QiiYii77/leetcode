class Solution:
    def build_list(self, nums: List[int]):
        n = len(nums)
        l = [0 for i in range(n)]
        for i in range(n):
            if i == 0:
                l[i] = nums[i]
            elif i == 1:
                l[i] = max(l[i-1], nums[i])
            else:
                l[i] = max(l[i-1], l[i-2] + nums[i])
        
        return l

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        elif n == 3:
            return max(nums[0], nums[1], nums[2])
        else:
            a = self.build_list(nums)
            b = self.build_list(nums[1:])
            # print(a)
            # print(b)
            # print(a[n-2])
            # print(b[n-3])
            # print(nums[n-1])
            return max(a[n-2], b[n-4]+nums[n-1])

