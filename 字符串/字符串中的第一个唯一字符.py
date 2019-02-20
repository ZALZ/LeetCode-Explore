'''


给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.


注意事项：您可以假定该字符串只包含小写字母。


'''


class Solution(object):
    @classmethod
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        first = len(s)
        li = [-2] * 26
        for index, value in enumerate(s):
            li[ord(value) - 97] = -1 if li[ord(value) - 97] != -2 else index
        print(li)

        if max(li)<0:
            return -1

        for i in li:
            if i >= 0 and i < first:
                first = i

        return first

a = Solution.firstUniqChar("cc")
print(a)
