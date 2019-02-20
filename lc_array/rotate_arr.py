class Solution(object):
    @classmethod
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)-1
        for i in range(k):
            n = nums.pop(l)
            nums.insert(0,n)



n = [1,2,3,4,5]
Solution.rotate(n,3)
print(n)