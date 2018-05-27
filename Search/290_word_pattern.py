# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-5-28 2:58'

'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(words) != len(pattern):
            return False
        p2w, w2p = {}, {}
        for i in range(len(words)):
            if p2w.get(pattern[i]) != w2p.get(words[i]):
                return False
            p2w[pattern[i]] = w2p[words[i]] = i
        # return True



if __name__ == "__main__":
    print(Solution().wordPattern("abba", "dog cat cat fish"))
