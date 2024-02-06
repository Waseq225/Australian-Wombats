class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        res = []
        for i in range(0,len(nums)-1, 2):
            res.append(nums[i+1])
            res.append(nums[i])
        return res