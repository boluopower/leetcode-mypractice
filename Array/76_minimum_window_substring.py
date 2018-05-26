# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-5-26 14:08'

'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "DVAOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''


class Solution:
    """
    Time: O(n)
    Space:O(k)
    """
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res, min_len, left = '', len(s) + 1, 0
        t_freq = {}
        for i in t:
            if (i in t_freq):
                t_freq[i] += 1
            else:
                t_freq[i] = 1
        crr_freq = {k: 0 for k in t}

        for i, v in enumerate(s):
            if v in t:
                crr_freq[v] += 1
            repeat = self.is_repeat(t_freq, crr_freq)
            if repeat:
                while (left <= i):
                    if s[left] in t:
                        crr_freq[s[left]] -= 1
                    left += 1
                    repeat = self.is_repeat(t_freq, crr_freq)
                    if not repeat:
                        if i - left + 2 < min_len:
                            res = s[left - 1:i + 1]
                            min_len = i - left + 2
                        break
        return res

    def is_repeat(self, t_freq, crr_freq):
        repeat = True
        for k, v in t_freq.items():
            if v > crr_freq[k]:
                repeat = False
                break
        return repeat


if __name__ == "__main__":
    print(Solution().minWindow("cabwefgewcwaefgcf", "cae"))
