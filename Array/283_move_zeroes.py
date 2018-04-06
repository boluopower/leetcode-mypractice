# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-3-31 21:20'
'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


class Solution:
    # 时间复杂度：O(n) 空间复杂度：O(1)
    def move_zeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while j < len(nums):
            if nums[j]:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        print(nums)


s = Solution()
s.move_zeroes([1, 0, 4, 0, 34, 0, 0, 34])
