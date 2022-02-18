class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        a = [[None for i in range(n)] for j in range(n)]
        for s in range(n):
            # print("s={}".format(s))
            for i in range(0,n-s):
                # print("i={}".format(i))
                if s == 0:
                    a[i][i+s] = nums[i]
                elif s == 1:
                    a[i][i+s] = max(a[i][i], a[i+s][i+s])
                else:
                    val_list = []
                    val_list.append(a[i+1][i+s])
                    # print("a[{}][{}] = {}".format(i+1,i+s, a[i+1][i+s]))
                    val_list.append(a[i][i+s-1])
                    # print("a[{}][{}] = {}".format(i, i+s-1, a[i][i+s-1]))
                    for k in range(i+1,i+s):
                        # print("a[{}][{}] = {}".format(i,k-1, a[i][k-1]))
                        # print("a[{}][{}] = {}".format(k+1, i+s, a[k+1][i+s]))
                        val_list.append(a[i][k-1] + a[k+1][i+s])
                    a[i][i+s] = max(val_list)

        # print(a)
        return a[0][n-1]

        # lenght = len(nums)
        # if lenght == 1:
        #     return nums[0]
        # else:
        #     rtn = 0
        #     for i in range(lenght):
        #         if i == 0:
        #             rval = self.rob(nums[i+1:])
        #             if rval > rtn:
        #                 rtn = rval
        #         elif i == lenght - 1:
        #             lval = self.rob(nums[:i])
        #             if lval > rtn:
        #                 rtn = lval
        #         else:
        #             lval = self.rob(nums[:i])
        #             rval = self.rob(nums[i+1:])
        #             if lval + rval > rtn:
        #                 rtn = lval + rval
        
        # return rtn
