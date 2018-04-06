# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-4-4 21:30'


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k):
            j = i + 1
            while j < len(nums):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums[k - 1]


s = Solution()
max_num = s.findKthLargest([-1,-1],2)
print(max_num)