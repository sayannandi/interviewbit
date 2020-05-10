class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        ans, curr = -1001, 0
        for num in A:
            curr += num
            ans = max(ans, curr)
            if curr <= 0:
                curr = 0
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([0]))