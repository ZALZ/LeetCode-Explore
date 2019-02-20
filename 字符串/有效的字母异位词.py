'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。
'''


class Solution(object):
    @classmethod
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ord_s = [0]*26
        ord_t = [0]*26

        for i in s:
            ord_s[ord(i)-97] += 1

        for i in t:
            ord_t[ord(i) - 97] += 1

        if  ord_s == ord_t:
            return True
        else:
            return False
