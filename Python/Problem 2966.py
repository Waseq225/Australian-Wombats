class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        new_list = sorted(nums)
        res = []
        for i in range(0, len(new_list), 3):
            if i + 2 < len(new_list):
                if new_list[i + 2] - new_list[i] > k:
                    return []
                res.append([new_list[i], new_list[i + 1], new_list[i + 2]])
        return res
