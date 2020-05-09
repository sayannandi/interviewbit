class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        steps = 0
        for i in range(1, len(A)):
            x = abs(A[i] - A[i - 1])
            y = abs(B[i] - B[i - 1])
            steps += max(x, y)
        return steps


if __name__ == '__main__':
    sol = Solution()
    print(sol.coverPoints([0, 1, 2], [0, 1, 2]))
