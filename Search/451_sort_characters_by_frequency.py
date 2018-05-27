# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-5-28 4:22'

'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = [(s.count(c), c) for c in set(s)]
        temp.sort(reverse=True)
        return ''.join([i[1] * i[0] for i in temp])
