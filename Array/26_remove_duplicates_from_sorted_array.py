# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-4-4 18:11'


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i += 1
                j += 1
        return len(nums)
