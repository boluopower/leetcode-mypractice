# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-4-5 1:07'


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        遍历目的是为了寻找更大的面积：当一边长一边短时，只有短边向中间移动面积才可能更大；当一样长时，只有两条边同时向中间移动面积才有可能最大。
        在此过程中，面积随时更新为更大的那个，当遍历结束时，面积自然时最大的。
        '''
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            max_area = max(max_area, (j - i) * (min(height[j], height[i])))
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return max_area
