from typing import List

# Time Limit Exceeded
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        return self.updateMatrixHelper(mat, 1)

    def updateMatrixHelper(self, mat: List[List[int]], height: int) -> List[List[int]]:
        copy = [[mat[i][j] for j in range(len(mat[0]))] for i in range(len(mat))]

        c = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] < height:
                    c += 1
                    continue

                isolated = True
                if i - 1 >= 0 and mat[i - 1][j] < height:
                    isolated = False
                if i + 1 < len(mat) and mat[i + 1][j] < height:
                    isolated = False
                if j - 1 >= 0 and mat[i][j - 1] < height:
                    isolated = False
                if j + 1 < len(mat[0]) and mat[i][j + 1] < height:
                    isolated = False

                if isolated:
                    copy[i][j] = height + 1

        return self.updateMatrixHelper(copy, height + 1) if c != len(mat) * len(mat[0]) else mat
