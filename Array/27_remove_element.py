# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-4-4 17:53'


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


s = Solution()
print(s.removeElement([2, 4, 1, 4, 4, 6, 4, 46, 2, 3, 2, 4], 4))
print(s.removeElement([4, 12, 3, 4, 2, 13, 4, 4, 3], 4))
