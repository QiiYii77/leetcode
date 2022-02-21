class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        a = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    if i not in a:
                        a[i] = [j]
                    else:
                        a[i].append(j)
        
        # print(a)

        l = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                l[len(nums)-1] = 1
            else:
                temp = 1
                if i in a:
                    for j in a[i]:
                        if l[j]+1 > temp:
                            temp = l[j]+1
                l[i] = temp
        
        # print(l)
        return max(l)
