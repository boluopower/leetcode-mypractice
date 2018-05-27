# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-5-28 4:14'

'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        # s2t, t2s = {}, {}
        # for i in range(len(t)):
        #     if s2t.get(s[i]) != t2s.get(t[i]):
        #         return False
        #     s2t[s[i]] = t2s[t[i]] = i
        # return True

if __name__ == "__main__":
    print(Solution().isIsomorphic("abba", "aega"))