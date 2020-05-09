class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        if n == 1:
            return -1
        for i, num in enumerate(A):
            A[i] = (num, i)
        A.sort()
        max_so_far = -1
        max_arr = [-1 for i in range(n)]
        for i in range(n - 1, -1, -1):
            max_arr[i] = max_so_far
            max_so_far = max(max_so_far, A[i][1])
        ans = -1
        for i, (_, idx) in enumerate(A):
            ans = max(ans, max_arr[i] - idx)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumGap([3, 5, 4, 2]))
