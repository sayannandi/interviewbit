class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)
        for idx, num in enumerate(A):
            if idx != n - 1 and num == A[idx + 1]:
                continue
            if num == n - idx - 1:
                return 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.solve([1, 2, 3, 4]))
