# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-3-31 20:17'

from time import time


# 在数组array中找到target并返回其索引
# 空间复杂度：O(1) 时间复杂度：O(log2n)
def binary_search(arr, target):
    n = len(arr)
    left = 0
    right = n - 1  # 确定边界：在[left, right]的范围里查找target
    while left <= right:  # 当left==right==last时，范围相当于[last, last]，此时相当于只有一个last未判断，由于是边界范围是闭区间，因此last也要进入循环
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1  # 由于范围是[left, right]，而target此时肯定在mid右边，因此用mid+1
        else:
            right = mid - 1  # 由于范围是[left, right]，而target此时肯定在mid左边，因此用mid-1
    return -1


res0 = binary_search([1, 3, 54, 67, 90], 1)
res1 = binary_search([1, 3, 54, 67, 90], 54)
res2 = binary_search([1, 3, 54, 67, 90], 90)
res3 = binary_search([1, 3, 54, 67, 90], 200)
print(res0, res1, res2, res3)
