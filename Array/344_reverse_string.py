# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-4-5 0:29'


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)


s = Solution()
print(s.reverseString('hello'))
