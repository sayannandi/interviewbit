class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        res = []
        for i in range(len(A)):
            x, y = 0, i
            curr = []
            while y >= 0:
                curr.append(A[x][y])
                x += 1
                y -= 1
            res.append(curr)
        for i in range(1, len(A)):
            x, y = i, len(A) - 1
            curr = []
            while x < len(A):
                curr.append(A[x][y])
                x += 1
                y -= 1
            res.append(curr)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
