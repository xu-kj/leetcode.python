from typing import List
import math

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        distance = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    continue

                d = math.inf
                if i - 1 >= 0:
                    d = min(d, distance[i - 1][j])
                if j - 1 >= 0:
                    d = min(d, distance[i][j - 1])
                distance[i][j] = d + 1

        for i in reversed(range(len(mat))):
            for j in reversed(range(len(mat[0]))):
                if mat[i][j] == 0:
                    continue

                d = math.inf
                if i + 1 < len(mat):
                    d = min(d, distance[i + 1][j])
                if j + 1 < len(mat[0]):
                    d = min(d, distance[i][j + 1])
                distance[i][j] = min(distance[i][j], d + 1)

        return distance
