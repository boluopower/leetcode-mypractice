# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-4-4 18:26'


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        while j < len(nums):
            i += 1
            j += 1
            if nums[i - 1] != nums[j - 1]:
                continue
            while j < len(nums) and nums[i] == nums[j]:
                nums.pop(j)
            i += 1
            j += 1
        print(nums)
        return len(nums)


s = Solution()
s.removeDuplicates([1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8])
