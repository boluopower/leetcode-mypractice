# -*- coding:utf-8 -*-
__author__ = 'yyp'
__date__ = '2018-5-27 18:09'


class Solution:
    """
    Time: O(n)
    Space:O(1)
    """
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        left, right = 0, len(p) - 1
        temp = [0] * 26
        for i in s[left:right + 1]:
            temp[ord(i)-ord('a')] += 1
        p_freq = [0] * 26
        for i in p:
            p_freq[ord(i) - ord('a')] += 1

        while right < len(s):
            if temp == p_freq:
                res.append(left)
            if (right + 1 < len(s)):
                temp[ord(s[left])-ord('a')] -= 1
                temp[ord(s[right + 1])-ord('a')] += 1
            left += 1
            right += 1
        return res


if __name__ == "__main__":
    print(Solution().findAnagrams("cbaebabacd", "abc"))
