class Solution(object):
    @classmethod
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)-1

        for i in range(int(len(matrix)/2)):
            for j in range(i,l-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[l-j][i]
                matrix[l - j][i] = matrix[l-i][l-j]
                matrix[l - i][l - j] = matrix[j][l-i]
                matrix[j][l - i] = temp
                print(matrix)



matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution.rotate(matrix)
print(matrix)