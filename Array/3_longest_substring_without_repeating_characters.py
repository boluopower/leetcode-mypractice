# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-5-26 3:42'

'''
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution:
    """
    Time: O(n)
    Space:O(1)
    """

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, res, freq = 0, 0, [False for _ in range(256)]
        for idx, char in enumerate(s):
            if freq[ord(char)]:
                while s[l] != char:
                    freq[ord(s[l])] = False
                    l += 1
                l += 1
            else:
                freq[ord(char)] = True
            res = max(idx - l + 1, res)
        return res
