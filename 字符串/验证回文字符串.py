'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:
输入: "race a car"
输出: false
'''

class Solution(object):
    @classmethod
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s)-1
        while(start<end):
            print(start, s[start], end, s[end],end="\t")
            print(ord(s[start]))
            if ord(s[start]) not in range(65,91) and ord(s[start]) not in range(97,123) and ord(s[start]) not in range(48,58):
                print("start++")
                start += 1
                continue
            if ord(s[end]) not in range(65,91) and ord(s[end]) not in range(97,123) and ord(s[end]) not in range(48,58):
                print("end--")
                end -= 1
                continue
            if start<=end:
                print("ok")
                if s[start].lower() != s[end].lower():
                    return False
            start += 1
            end -= 1
        return True

print(Solution.isPalindrome("0P"))