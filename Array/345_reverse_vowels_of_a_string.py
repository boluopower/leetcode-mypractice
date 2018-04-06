# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-4-5 0:44'


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            if not self._is_vowel(s[i]):
                i += 1
                continue
            if not self._is_vowel(s[j]):
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)

    def _is_vowel(self, c):
        if c in "aeiouAEIOU":
            return True


s = Solution()
print(s.reverseVowels('aA'))
