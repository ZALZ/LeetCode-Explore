'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

'''

class Solution(object):
    @classmethod
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pre = False
        if x<0:
            pre = True
            x = -x

        x = list(str(x))
        x.reverse()
        while True:
            if x[0] == "0":
                x.pop(0)
            else:
                break

        if pre:
            x.insert(0,"-")
        s=""
        for i in x:
           s+=i
        x = int(s)
        return x

x = Solution.reverse(-100)
print(x)





