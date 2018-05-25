# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-5-26 4:35'

'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: [2,3,1,2,4,3], s = 7
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n)
'''


class Solution:
    """
    Time: O(n)
    Space:O(1)
    """

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        # 超时的写法
        # l = len(nums)
        # res, left = l + 1, 0
        # for i in range(l):
        #     while sum(nums[left:i + 1]) >= s and left <= i:
        #         res = min(res, i - left + 1)
        #         left += 1
        # return res if res != l + 1 else 0

        l = len(nums)
        res, left, my_sum = l + 1, 0, 0
        for i in range(l):
            my_sum += nums[i]
            while my_sum >= s:
                res = min(res, i - left + 1)
                my_sum -= nums[left]
                left += 1
        return res if res != l + 1 else 0
