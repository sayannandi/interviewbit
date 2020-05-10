class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        res = [[-1 for i in range(A)] for j in range(A)]
        dir_x = [0, 1, 0, -1]
        dir_y = [1, 0, -1, 0]
        num, i, j, slides = 1, 0, 0, 0
        while num <= A * A:
            res[i][j] = num
            num += 1
            x = dir_x[slides % 4]
            y = dir_y[slides % 4]
            if i + x < 0 or i + x >= A or j + y < 0 or j + y >= A or res[i + x][j + y] != -1:
                slides += 1
                i += dir_x[slides % 4]
                j += dir_y[slides % 4]
            else:
                i += x
                j += y
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateMatrix(5))
