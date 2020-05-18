class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        zrows = set()
        zcols = set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 0:
                    zrows.add(i)
                    zcols.add(j)
        for r in zrows:
            for i in range(len(A[0])):
                A[r][i] = 0
        for c in zcols:
            for i in range(len(A)):
                A[i][c] = 0
        return A


if __name__ == '__main__':
    sol = Solution()
    print(sol.setZeroes([[1, 0, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1]]))
