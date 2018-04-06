# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-4-4 23:22'


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        raise Exception('this input has no solution')


s = Solution()
print(s.twoSum([1, 3], 2))