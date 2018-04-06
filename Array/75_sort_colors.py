# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-3-31 23:14'
'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note:
You are not suppose to use the library's sort function for this problem.
'''


# 此处使用三路快排，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # [0, zero] [zero+1, two-1] [two,n-1]
        n = len(nums)
        zero = -1
        two = n
        i = 0
        while i < two:
            if nums[i] == 0:
                zero += 1
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                two -= 1
                nums[two], nums[i] = nums[i], nums[two]
        print(nums)


s = Solution()
s.sortColors([0, 2, 1, 0, 0, 1, 1, 1, 2, 0, 2, 1])
