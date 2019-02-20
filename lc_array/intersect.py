class Solution(object):
    @classmethod
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        num1_dic = {}
        res = []
        for i in nums1:
            if i in num1_dic.keys():
                num1_dic[i]+=1
            else:
                num1_dic[i]=1
        for i in nums2:
            if i in num1_dic.keys() and num1_dic[i]>0:
                res.append(i)
                num1_dic[i]-=1
        return res


l1 = [1,4,9,5]
l2 = [9,4,9,8,4]
sub = Solution.intersect(l1,l2)
print(sub)