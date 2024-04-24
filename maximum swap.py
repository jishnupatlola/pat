class Solution:
    def maximumSwap(self, num: int) -> int:
        nums=[int(i) for i in str(num)]
        dict={}
        for i,j in enumerate(nums):
            dict[j]=i
        for i in range(len(nums)):
            for j in range(9,nums[i],-1):
                if j in dict and dict[j]>i:
                    nums[i],nums[dict[j]]=nums[dict[j]],nums[i]
                    return int("".join(map(str,nums)))
        return num
