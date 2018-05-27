# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-5-28 0:48'

'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?


'''


class Solution:
    """
    Time: O()
    Space:O()
    """
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import defaultdict
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)
        for i in s:
            s_freq[i] += 1
        for i in t:
            t_freq[i] += 1
        return s_freq == t_freq
