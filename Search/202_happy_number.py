# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-5-28 1:24'

'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        repeat = {}
        while n != 1 and n not in repeat:
            repeat[n] = True
            n = sum(map(lambda i: int(i) * int(i), str(n)))
        return n == 1


if __name__ == "__main__":
    print(Solution().isHappy(19))
